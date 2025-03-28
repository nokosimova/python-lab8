import grpc
from concurrent import futures
from google.protobuf import empty_pb2
from grpc_reflection.v1alpha import reflection

from .database import Base, engine_db, SessionLocal
from . import repository

import app_pb2
import app_pb2_grpc

class GlossaryService(app_pb2_grpc.GlossaryServiceServicer):
    
    def CreateWord(self, rqst, cnxt):
        
        with SessionLocal() as db:
            
            word = repository.get_word_by_name(db, rqst.word.name)
            
            if word:
                cnxt.set_code(grpc.StatusCode.ALREADY_EXISTS)
            
                return app_pb2.WordResponse()

            new_word = repository.add_word(db, rqst.word.name, rqst.word.definition)
            
            return app_pb2.WordResponse(word = app_pb2.Word(name = new_word.name, definition = new_word.definition))

    def GetWord(self, rqst, cnxt):
        
        with SessionLocal() as db:
        
            word = repository.get_word_by_name(db, rqst.name)
        
            if not word:
        
                cnxt.set_code(grpc.StatusCode.NOT_FOUND)
        
                return app_pb2.WordResponse()

            return app_pb2.WordResponse(word=app_pb2.Word(name = word.name, definition=word.definition))

    def DeleteWord(self, rqst, cnxt):

        with SessionLocal() as db:

            repository.delete_word(db, rqst.id)
            
            return empty_pb2.Empty()

    def UpdateWord(self, rqst, cnxt):
    
        with SessionLocal() as db:
    
            word = repository.get_word_by_name(db, rqst.word.name)
    
            if not word:
    
                cnxt.set_code(grpc.StatusCode.NOT_FOUND)
    
                return app_pb2.WordResponse()

            updated_word = repository.update_word(db, word.name, rqst.word.definition)
    
            return app_pb2.WordResponse(word = app_pb2.Word(name = updated_word.name, definition = updated_word.definition))

    def ListAllWords(self, rqst, cnxt):

        with SessionLocal() as db:

            words_list = repository.get_all_words(db)
            result = []
            #parse result:
            for w in words_list:
                result.append(app_pb2.Word(id = w.id, name = w.name, definition = w.definition))
            
            return app_pb2.ListResponse(words=result)

Base.metadata.create_all(bind=engine_db)

def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=14))
    app_pb2_grpc.add_GlossaryServiceServicer_to_server(GlossaryService(), server)

    # Enable reflection
    reflection.enable_server_reflection((
        app_pb2.DESCRIPTOR.services_by_name['GlossaryService'].full_name,
        reflection.SERVICE_NAME), 
        server)

    server.add_insecure_port('[::]:8000')
    
    server.start()

    print("gRPC сервер запущен на порту 8000")

    server.wait_for_termination()


if __name__ == "__main__":
    start()