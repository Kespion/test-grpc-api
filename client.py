import grpc
from device_pb2 import Device, GetAllDevicesRequest, GetDeviceByIdRequest, AddDeviceRequest, UpdateDeviceRequest, DeleteDeviceRequest
from device_pb2_grpc import DeviceServiceStub


def add_device(stub: DeviceServiceStub, device: Device):
    response_add = stub.AddDevice(AddDeviceRequest(device=device))
    print("Added device:", response_add)


def get_device_by_id(stub: DeviceServiceStub, id: int):
    response_get_by_id = stub.GetDeviceById(GetDeviceByIdRequest(id=id))
    print("GetDeviceById Response:", response_get_by_id)


def get_all_devices(stub: DeviceServiceStub):
    response_get_all = stub.GetAllDevices(GetAllDevicesRequest())
    print("GetAllDevices Response:", response_get_all)


def update_device(stub: DeviceServiceStub, id: int, device: Device):
    response_update = stub.UpdateDevice(UpdateDeviceRequest(id=id, device=device))
    print("UpdateDevice Response:", response_update)


def delete_device(stub: DeviceServiceStub, id: int):
    response_delete = stub.DeleteDevice(DeleteDeviceRequest(id=id))
    print("DeleteDevice Response:", response_delete)


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = DeviceServiceStub(channel)

        #  print("\n======= Add a device =======\n")
        #  add_device(stub, Device(
        #      name="Device name",
        #      brand="Device brand",
        #      model="Device model",
        #      os="Device OS",
        #      version="Device Version",
        #      wifi=True,
        #      bluetooth=False
        #  ))

        #  print("\n======= Get a device by its ID =======\n")
        #  get_device_by_id(stub, 1)

        #  print("\n======= Update a device =======\n")
        #  update_device(stub, 1, Device(
        #      name="Device name updated",
        #      brand="Device brand updated",
        #      model="Device model updated",
        #      os="Device OS updated",
        #      version="Device Version updated",
        #      wifi=False,
        #      bluetooth=True
        #  ))

        #  print("\n======= Delete a device by ID =======\n")
        #  delete_device(stub, 2)

        print("\n======= Get all devices =======\n")
        get_all_devices(stub)
