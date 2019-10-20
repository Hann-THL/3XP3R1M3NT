from datetime import datetime



def show_date(prefix):
    print(f'[SCRIPT-OUTPUT] - {prefix} at {datetime.now()}')

def show_output():
    print('[SCRIPT-OUTPUT] - script3.py ask: Why don\'t you find me ?!!')

def main():
    show_date('Start')
    show_output()
    show_date('End')



if __name__ == "__main__":
    main()