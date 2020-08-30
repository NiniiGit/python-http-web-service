import BaseHTTPServer
import SimpleHTTPServer
import os
server_address = ("", 8081)
PUBLIC_RESOURCE_PREFIX = '/folder_web/'
MANAGER_RESOURCE_PREFIX = '/folder/manager.log'
#PUBLIC_DIRECTORY = '/path/to/protected/public'
PUBLIC_Manager_log = '/<your_folder_path>/logs/folder_web/'
#PUBLIC_Manager_log = '/<your_folder_path>/logs/_Manager/'
folder_initialload_dir='/<your_folder_path>/logs/initialload/'
folder_manager_dir='/<your_folder_path>/logs/_Manager/'

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if self.path.startswith(PUBLIC_RESOURCE_PREFIX):

             if self.path == '/folder_web/folder_manager_dir/' or self.path == '/folder_web/folder_manager_dir/manager.log/':
                        
                        if self.path == '/folder_web/folder_manager_dir/manager.log/':
                                return folder_manager_dir+'manager.log'
                        else:
                                return folder_manager_dir
                                #print(folder_manager_dir+'manager.log')


elif self.path == '/folder_web/folder_initialload_dir/' or self.path == "/folder_web/folder_initialload_dir/*.log":
                      
                        if self.path == "/folder_web/folder_initialload_dir/*.log/":
                                return  folder_initialload_dir+'*.log'
                                print(folder_initialload_dir+'*.log')
                        else:
                                return folder_initialload_dir
                                print(folder_initialload_dir)
                      
#  if self.path == PUBLIC_RESOURCE_PREFIX or self.path == PUBLIC_RESOURCE_PREFIX + '/':     

             else:
                return PUBLIC_Manager_log

   #     if self.path.startswith(MANAGER_RESOURCE_PREFIX):

        #       return PUBLIC_Manager_log+'manager.log'
#+ '/*.log'
           # else:
            #    return PUBLIC_DIRECTORY + path[len(PUBLIC_RESOURCE_PREFIX):]
        else:
            return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self, path)

httpd = BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
httpd.serve_forever()
