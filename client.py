import grpc
from device_pb2 import Device, GetAllDevicesRequest, GetDeviceByIdRequest, AddDeviceRequest, UpdateDeviceRequest, DeleteDeviceRequest
from device_pb2_grpc import DeviceServiceStub


def run():
    with grpc.insecure_channel('192.168.1.22:50051') as channel:
        stub = DeviceServiceStub(channel)

        #  # Ajoutez un périphérique
        #  new_device = Device(
        #      name="Antho/Kespute",
        #      brand="Samsung",
        #      model="Galaxy A52S",
        #      os="Android",
        #      version="14",
        #      wifi=True,
        #      bluetooth=True
        #  )
        #  response_add = stub.AddDevice(AddDeviceRequest(device=new_device))
        #  print("Added device:", response_add)

        #  # Récupérez le périphérique par ID
        #  response_get_by_id = stub.GetDeviceById(GetDeviceByIdRequest(id=1))
        #  print("GetDeviceById Response:", response_get_by_id)

        #  # Test UpdateDevice
        #  updated_device = Device(
        #      name="UpdatedDevice",
        #      brand="UpdatedBrand",
        #      model="UpdatedModel",
        #      os="UpdatedOS",
        #      version="UpdatedVersion",
        #      wifi=True,
        #      bluetooth=True
        #  )
        #  response_update = stub.UpdateDevice(UpdateDeviceRequest(id=1, device=updated_device))
        #  print("UpdateDevice Response:", response_update)

        #  # Test DeleteDevice
        #  response_delete = stub.DeleteDevice(DeleteDeviceRequest(id=3))
        #  print("DeleteDevice Response:", response_delete)

        # Test GetAllDevices
        response_get_all = stub.GetAllDevices(GetAllDevicesRequest())
        print("GetAllDevices Response:", response_get_all)


if __name__ == '__main__':
    run()
