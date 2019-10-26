import argparse
import sys
import pathlib
import os

def parse_args(args):
    parser = argparse.ArgumentParser('Extracts Java code for Sphinx')
    parser.add_argument('-i', '--input', help='input directory', required=False, default='source/code/src/main/java/com/oneoffcoder/java')
    parser.add_argument('-o', '--output', help='output directory', required=False, default='source/java')
    return parser.parse_args(args)

def get_output_file(output, file_path):
    def trim(file_path):
        path = str(file_path)
        stem = 'src/main/java/'
        idx = path.index(stem)
        
        start = idx + len(stem)
        end = len(path)
        
        p = path[start:end]
        
        return p

    return f'{output}/{trim(file_path)}'

def get_output_dir(output_file):
    index = output_file.rindex('/')
    return output_file[0:index]

def get_imports(lines):
    return ''.join([line for line in lines if line.startswith('import')])

def get_main_code(lines):
    def get_start(lines):
        for i, line in enumerate(lines):
            if line.strip().startswith('public static void main'):
                return i + 1
    
    def get_end(lines):
        counter = 0
        for i, line in enumerate(reversed(lines)):
            if line.strip() == '}':
                counter += 1
            if counter == 2:
                return len(lines) - i - 1
    
    def get_code_lines(lines):
        start = get_start(lines)
        end = get_end(lines)
        return lines[start:end]

    format = lambda line: line[4:len(line)] if line != '\n' else line

    main_lines = get_code_lines(lines)
    main_lines = [format(line) for line in main_lines]
    
    return ''.join(main_lines)

def get_supporting_code(lines):
    def get_start(lines):
        for i, line in enumerate(lines):
            if line.strip().startswith('public class'):
                return i + 1
    
    def get_end(lines):
        for i, line in enumerate(lines):
            if line.strip().startswith('public static void main'):
                return i - 1
    
    def get_code_lines(lines):
        start = get_start(lines)
        end = get_end(lines)
        return lines[start:end]
    
    format = lambda line: line[2:len(line)] if line != '\n' else line

    support_lines = get_code_lines(lines)
    support_lines = [format(line) for line in support_lines]

    return ''.join(support_lines)

def get_lines(file_path):
    with open(file_path, 'r') as f:
        return [line for line in f]

def parse_file(file_path):
    lines = get_lines(file_path)
        
    imps = get_imports(lines)    
    support = get_supporting_code(lines)    
    main = get_main_code(lines)

    if len(imps.strip()) == 0 and len(support.strip()) == 0:
        return main
    elif len(imps.strip()) > 0 and len(support.strip()) == 0:
        return '\n'.join([imps, main])
    elif len(imps.strip()) == 0 and len(support.strip()) > 0:
        return '\n'.join([support, '// test code', main])
    else:
        return '\n'.join([imps, support, '//test code', main])

def start_extraction(input, output):
    print(f'extracting from {input} => {output}')
    print()

    java_files = pathlib.Path(input).glob('**/*.java')
    for java_file in java_files:
        output_file = get_output_file(output, java_file)
        output_dir = get_output_dir(output_file)

        print(f'parsing {java_file} => {output_file}')
        print(output_dir)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        code = parse_file(java_file)
        # print(code.strip())
        with open(output_file, 'w') as f:
            f.write(code.strip())

        # break

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    start_extraction(args.input, args.output)
    # print(parse_file('source/code/src/main/java/com/oneoffcoder/java/clazz/Basic.java'))
