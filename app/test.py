import grpc
from google.protobuf import empty_pb2

import app_pb2
import app_pb2_grpc

def run():
    with grpc.insecure_channel('127.0.0.1:8000') as channel:
        st = app_pb2_grpc.GlossaryServiceStub(channel)

        print("ListAll:", st.ListAllWords(empty_pb2.Empty()).words)
        
        print("Create 1:", st.CreateWord(app_pb2.CreateWordRequest(word = app_pb2.Word(name = "python", definition = "Programming language"))))
        
        print("Create 2:", st.CreateWord(app_pb2.CreateWordRequest(word = app_pb2.Word(name = "terraform", definition = "Infrastructure as code tool"))))


        print("Get:", st.GetWord(app_pb2.GetWordRequest(name = "python")))
        
        print("Update:", st.UpdateWord(app_pb2.UpdateWordRequest(word = app_pb2.Word(name = "python", definition = "Высокоуровневый язык"))))
        
        print("ListAll:", st.ListAllWords(empty_pb2.Empty()))
        
        st.DeleteWord(app_pb2.DeleteWordRequest(id = 1))
        
        print("Word 'python' was deleted")
        
        print("ListAll after deleting operation:", st.ListAllWords(empty_pb2.Empty()))
        
        #clear all test data:
        for word in st.ListAllWords(empty_pb2.Empty()).words:
            print(word.id)
            st.DeleteWord(app_pb2.DeleteWordRequest(id = word.id))


if __name__ == "__main__":
    run()