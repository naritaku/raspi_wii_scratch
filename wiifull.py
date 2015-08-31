import cwiid,time,math,scratch
s = scratch.Scratch()
button_delay = 0.3

print 'Please press buttons 1 + 2 on your Wiimote now ...'
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!"
  quit()

print 'Wiimote connection established!\n'
print 'Go ahead and press some buttons\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'
wii.rpt_mode =cwiid.RPT_IR | cwiid.RPT_ACC | cwiid.RPT_BTN
time.sleep(3)

a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n = ["left","right","up","down","1","2","a","b","home","minus","plus","acc_X","acc_Y","acc_Z","accel","IR_X","IR_Y","IR"]
i=0
while True:
  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
  if (buttons & cwiid.BTN_LEFT):
    a[0]=1
  if(buttons & cwiid.BTN_RIGHT):
    a[1]=1
  if (buttons & cwiid.BTN_UP):
    a[2]=1
  if (buttons & cwiid.BTN_DOWN):
    a[3]=1
  if (buttons & cwiid.BTN_1):
    a[4]=1
  if (buttons & cwiid.BTN_2):
    a[5]=1
  if (buttons & cwiid.BTN_A):
    a[6]=1
  if (buttons & cwiid.BTN_B):
    a[7]=1
  if (buttons & cwiid.BTN_HOME):
    a[8]=1
  if (buttons & cwiid.BTN_MINUS):
    a[9]=1
  if (buttons & cwiid.BTN_PLUS):
    a[10]=1
  accel=wii.state['acc']
  a[11]=accel[0]
  a[12]=accel[1]
  a[13]=accel[2]
  a[14]=round(math.sqrt(a[11]**2+a[12]**2+a[13]**2))
  ir=wii.state['ir_src'][0]
  if isinstance(ir,type(None)):
    a[17]=0
  else :
    a[15]=(ir.values()[0][0]-500)*-0.5
    a[16]=(ir.values()[0][1]-530)*-1.2
    a[17]=1
  s.sensorupdate({n[0]:a[0],n[1]:a[1],n[2]:a[2],n[3]:a[3],n[4]:a[4],n[5]:a[5],n[6]:a[6],n[7]:a[7],n[8]:a[8],n[9]:a[9],n[10]:a[10],n[11]:a[11],n[12]:a[12],n[13]:a[13],n[14]:a[14],n[15]:a[15],n[16]:a[16],n[17]:a[17]})
  for i in range(11):
    a[i]=0
  time.sleep(button_delay)
