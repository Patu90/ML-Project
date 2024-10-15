import sys
import logging

def error_message_detail(error,error_detil:sys):
    _,_,exc_tb=error_detil.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line numbern[{1}] error message[{2}]".format()
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
    
class CustomException(Exception):
    def__init__(self,error_message,error_detil:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detil=error_detail)
    
    def __str__(self):
        return self.error_message   
    
    

    