# test grpc server
import grpc
import iq180_pb2_grpc
import iq180_pb2

# connect to server
host_ip = 'eteownserver.thddns.net'
channel = grpc.insecure_channel(host_ip + ':3882')
stub = iq180_pb2_grpc.IQ180Stub(channel)
print("please enter your name:  ", end="")
player_name = input()

# enter game
enter_game_request = iq180_pb2.EnterGameRequest(name=player_name)
enter_game_response = stub.EnterGame(enter_game_request)
print(enter_game_response)
