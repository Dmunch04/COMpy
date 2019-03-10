def load (path):
    if not path.endswith('.com'):
        print('Given file is not a COM file!')
        path += '.com'

    file = open(path, 'r')
    raw = file.readlines()
    file.close()

    results = []

    for line in raw:
        for i, item in enumerate(line):
            if item == '{':
                for ni, nitem in enumerate(line):
                    if nitem == '}':
                        if line[ni + 1] == ';':
                            cur_line = line[i + 1 : ni].split('=')

                            for a, li in enumerate(cur_line):
                                cur_line[a] = cur_line[a].replace("'", '')
                                cur_line[a] = cur_line[a].replace(' ', '')

                            try:
                                res = (cur_line[0], cur_line[1])
                            except:
                                print('Something went wrong')

                            results.append(res)

    results = dict([i[:: + 1] for i in results])

    return results

def overload (path):
    data = load(path)

    elements = ''

    for element in data:
        elements += '{0}: {1}\n'.format(element, data[element])

    return elements

def string (text):
    return "'{0}'".format(text)
