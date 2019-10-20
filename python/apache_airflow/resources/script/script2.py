from datetime import datetime



def show_date(prefix):
    print(f'[SCRIPT-OUTPUT] - {prefix} at {datetime.now()}')

def show_output():
    print('[SCRIPT-OUTPUT] - script2.py replied: I\'m here')

def main():
    show_date('Start')
    show_output()
    show_date('End')



if __name__ == "__main__":
    main()