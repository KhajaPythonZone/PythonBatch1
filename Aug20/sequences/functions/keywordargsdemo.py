
def print_kwargs(**kwargs):
    print('Keyword arguments: ', kwargs)
    print(f'Type of Keyword arguments {type(kwargs)}')
    

if __name__ == "__main__":
    print_kwargs()
    print_kwargs(course='python', trainer='khaja', institute='Quality Thought')