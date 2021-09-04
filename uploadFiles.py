
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)


                relative_path = os.path.relpath(local_path, file_from)
                dropbox.path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A2QMHmmO0McOWSAP_S7wDAKDzrS5CH_qMZqOJuvQiw96PPu6dNqzfkFg9C_i33m_zD15DdVbTKLi2Z5waY-k37Fc40PyaD8avkBes8LKr3nMO7aKvUPb7ov0B8cW5V5fTrEpb8s'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer :- "))
    file_to = input("Enter the full path to upload to dropbox:- ")


    transferData.upload_file(file_from,file_to)
    print("file has been removed !!!")

main()