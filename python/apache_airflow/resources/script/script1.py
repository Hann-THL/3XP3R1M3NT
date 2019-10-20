from datetime import datetime



def show_date(prefix):
    print(f'[SCRIPT-OUTPUT] - {prefix} at {datetime.now()}')

def show_output():
    print('[SCRIPT-OUTPUT] - script1.py asked: Where are you script2 ???')

def main():
    show_date('Start')
    show_output()
    show_date('End')



if __name__ == "__main__":
    main()