import grpc
from concurrent import futures
import sqlite3
from device_pb2 import Device, AllDevicesResponse, DeleteDeviceResponse
from device_pb2_grpc import DeviceServiceServicer, add_DeviceServiceServicer_to_server

DATABASE_FILE = "devices.db"


class DeviceServiceImplementation(DeviceServiceServicer):
    def __init__(self):
        self.conn = None

    def _get_connection(self):
        return sqlite3.connect(DATABASE_FILE)

    def GetDeviceById(self, request, context):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM devices WHERE id=?", (request.id,))
            row = cursor.fetchone()
            if row:
                return Device(
                    id=row[0],
                    name=row[1],
                    brand=row[2],
                    model=row[3],
                    os=row[4],
                    version=row[5],
                    wifi=row[6],
                    bluetooth=row[7]
                )
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Device not found")
                return Device()

    def GetAllDevices(self, request, context):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM devices")
            devices = [Device(
                id=row[0],
                name=row[1],
                brand=row[2],
                model=row[3],
                os=row[4],
                version=row[5],
                wifi=row[6],
                bluetooth=row[7]
            ) for row in cursor.fetchall()]
            return AllDevicesResponse(devices=devices)

    def AddDevice(self, request, context):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO devices (name, brand, model, os, version, wifi, bluetooth)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (request.device.name, request.device.brand, request.device.model,
                  request.device.os, request.device.version, request.device.wifi, request.device.bluetooth))
            conn.commit()
            return request.device

    def UpdateDevice(self, request, context):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE devices
                SET name=?, brand=?, model=?, os=?, version=?, wifi=?, bluetooth=?
                WHERE id=?
            ''', (request.device.name, request.device.brand, request.device.model,
                  request.device.os, request.device.version, request.device.wifi,
                  request.device.bluetooth, request.id))
            conn.commit()
            return request.device

    def DeleteDevice(self, request, context):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM devices WHERE id=?", (request.id,))
            conn.commit()
            return DeleteDeviceResponse(success=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DeviceServiceServicer_to_server(DeviceServiceImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
