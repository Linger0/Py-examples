class CallMe:
  def __init__(this, val):
    this.value = val
  def call_me(this):
    print(this.value)

class InstMe:
  def __init__(this, val):
    this.value = val

inst_me = InstMe(1)
CallMe.call_me(inst_me)
