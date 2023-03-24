import sys

def error_message_details(error,error_detail:sys):
    # exc_tb will give information like on which file the exception has occured and on which line exception has occured
    _,_,exc_tb = error_detail.exc_info()

    # in which file name error is present
    file_name = exc_tb.tb_frame.f_code.co_filename

    # line number
    line_number = exc_tb.tb_lineno

    # error message
    error_message = str(error)

    # Final Error Message
    error_msg = "Error Occured in Python Script name [{0}] line number [{1}] error message : [{2}]".format(
      file_name, line_number,error_message
    )
    return error_msg

# creating a CUSTOM Exception class
# Exception is the SUPER class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        # We are inheriting the error_message from SUPER CLass which is Exception class
        super.__init__(error_message)
        self.error_message = error_message_details(error_message , error_detail=error_detail)

    def __str__(self):
        return self.error_message
