import re


def normalize(value):

    if value is None:
        return ""

    value = str(value)

    # LOWERCASE
    value = value.lower()

    # REMOVE EXTRA SPACES
    value = " ".join(
        value.split()
    )

    # REMOVE SPACES AROUND SPECIAL CHARACTERS
    value = re.sub(
        r"\s*([,:;()\-\/])\s*",
        r"\1",
        value
    )

    # REMOVE COMMAS
    value = value.replace(",", "")

    # NUMBER NORMALIZATION
    try:

        number = float(value)

        if number.is_integer():

            value = str(
                int(number)
            )

    except:
        pass

    return value