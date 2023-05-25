from collections import namedtuple

Accumulator = namedtuple(""Accumulator"", [""age"", ""count""])

def head(records):
    return records[0]

def tail(records):
    return records[1:]

def accumulate_age(record, accumulator):
    return Accumulator(accumulator.age + record[""age""], accumulator.count + 1) if ""age"" in record else accumulator

def meanAge(records, accumulator=Accumulator(0, 0)):
    if not records:
        return None
    if len(records) == 1:
        result = accumulate_age(head(records), accumulator)
        return result.age / result.count

    return meanAge(tail(records), accumulate_age(head(records), accumulator)) 