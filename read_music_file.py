def read_file(file_name):
    """
    This function returns data about a music file
    file_name : str - file name, for processing 
    """
    with open(file_name, 'rb') as f:
        f.seek(-128, 2)
        if f.read(3).decode(encoding='utf-8') == 'TAG':
            print('Title : ', f.read(30).decode())
            print('Аrtist : ', f.read(30).decode())
            print('Album : ', f.read(30).decode())
            print('Year : ', f.read(4).decode())

read_file('music.mp3')

