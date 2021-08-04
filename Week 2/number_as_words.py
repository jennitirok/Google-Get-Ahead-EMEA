ONES_AND_TEENS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
          'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
          'nineteen']

TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

SUFFIXES = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']

def under_one_thousand(amount: int) -> str:
  to_words = []
  # Tuple unpack the 'hundred' and the 'tens'
  hundred, tens = divmod(amount, 100)

  if ONES_AND_TEENS[hundred] != '':
    to_words.append(f"{ONES_AND_TEENS[hundred]} hundred")

  if tens < 20: 
    to_words.append(ONES_AND_TEENS[tens])
  else:
    sub_tens, sub_ones = divmod(tens, 10)
    to_words.append(TENS[sub_tens])
    to_words.append(ONES_AND_TEENS[sub_ones])

  # Return the concatenated strings in to_words list
  return ' '.join(to_words).rstrip()


def get_amount_in_words(amount: int) -> str:
  to_words = []
  suffix_counter = 0

  if amount == 0:
    return 'zero'

  while amount > 0:
    # Grab the integer in groups of three, backwards
    group = amount % 1000
    to_words.append(under_one_thousand(group))
    suffix_counter += 1
    amount = amount // 1000

  # Add the suffixes
  for i in range(0, suffix_counter):
    to_words[i] = (f"{to_words[i]} {SUFFIXES[i]}")

  # Reverse the contents of to_words list
  to_words = to_words[::-1]

  del amount

  # Return the concatenated strings in to_words list
  return ' '.join(to_words).rstrip()

