from rest_framework.views import exception_handler
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            'mensaje': 
                
             response.data
            
        }
        response.data = custom_response_data

    return response