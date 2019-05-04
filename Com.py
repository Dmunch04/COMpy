def Load (_Path):
    with open (_Path, 'r') as File:
        return Loads (File.read ())

def Loads (_Data):
    if isinstance (_Data, str):
        Data = _Data.split ('\n')

    else:
        Data = _Data

    Contents = {}
    LineIndex = 0

    for Line in Data:
        LineIndex += 1

        if Line in ' \n\t':
            continue

        FixedLine = Line.replace (' ', '').replace ('\n', '').replace ('\t', '')
        Length = len (FixedLine)
        Start = FixedLine[0]
        End = FixedLine[Length - 2]
        EOL = FixedLine[Length - 1]

        if EOL != ';':
            print ('Missing a ";" on line:', LineIndex)
            continue

        if Start == '{' and End == '}':
            Splitted = FixedLine[1 : Length - 2].split ('=')

            Key = Splitted[0][1 : len (Splitted[0]) - 1]
            Value = Splitted[1]

            if not (Value.startswith ("'") and Value.endswith ("'") or Value.startswith ('"') and Value.endswith ('"')):
                try:
                    Value = int (Value)

                except:
                    try:
                        Value = float (Value)

                    except:
                        if not Value.lower () in ['true', 'false', 'none', 'null']:
                            if Value in Contents:
                                Value = f"'{Contents[Value]}'"

                            else:
                                print ('No Key Found:', Value)
                                return

                        else:
                            if Value.lower () == 'true':
                                Value = True

                            elif Value.lower () == 'false':
                                Value = False

                            elif Value.lower () == 'none' or Value.lower () == 'null':
                                Value = None

            if not (isinstance (Value, int) or isinstance (Value, float) or Value.lower () in ['true', 'false']):
                Value = Value[1 : len (Value) - 1]

            Contents[Key] = Value

    return Contents
