import vertica_sdk
from base64 import b64decode

class base64_decode(vertica_sdk.ScalarFunction):
    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        while(True):
            data = arg_reader.getString(0)
            bin = b64decode(data)
            res_writer.setBinary(bin)
            res_writer.next()
            if not arg_reader.next():
                break

    def destroy(self, server_interface, col_types):
        pass

class base64_convert_factory(vertica_sdk.ScalarFunctionFactory):

    def createScalarFunction(self, srv):
        return base64_decode()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarbinary()
        return_type.addVarbinary()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarbinary(8192)
