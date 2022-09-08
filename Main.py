import random
import pyperclip
def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

def crosshairgen():
    color = ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    outline = random.randint(0,1)
    outlinethickness = random.randint(1,6)
    outlineocap= float("{0:.3f}".format(random.uniform(0, 1)))
    dot = random.randint(0,1)
    dotsize = random.randint(1,6)
    innerline = 1
    innerlineocap = float("{0:.3f}".format(random.uniform(0, 1)))
    innerlinelen = random.randint(0,20)
    innerlinelen2 = random.randint(0,20)
    innerlinethick = random.randint(0,10)
    innerlineoffset = random.randint(0,20)
    innerlinemovmenterr = random.randint(0,1)
    innerlinemovmentmultiply = float("{0:.3f}".format(random.uniform(0, 3)))
    innerlinefireerror = random.randint(0,1)
    innerlinefireerrormultiply = float("{0:.3f}".format(random.uniform(0, 3)))
    outerline = 1
    outerlineocap = float("{0:.3f}".format(random.uniform(0, 1)))
    outerlinelen = random.randint(0,20)
    outerlinelen2 = random.randint(0,20)
    outerlinethick = random.randint(0,10)
    outerlineoffset = random.randint(0,20)
    outerlinemovementerr = random.randint(0,1)
    outerlinemovementerrval= float("{0:.3f}".format(random.uniform(0, 3)))
    outterlinefiringeror = random.randint(0,1)
    outerlinefirringerrmultiply = float("{0:.3f}".format(random.uniform(0, 3)))
    ADS_color = ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    ADS_outline = random.randint(0,1)
    ADS_outlinethickness = random.randint(1,6)
    ADS_outlineocap= float("{0:.3f}".format(random.uniform(0, 1)))
    ADS_dot = random.randint(0,1)
    ADS_dotsize = random.randint(1,6)
    ADS_innerline = 1
    ADS_innerlineocap = float("{0:.3f}".format(random.uniform(0, 1)))
    ADS_innerlinelen = random.randint(0,20)
    ADS_innerlinelen2 = random.randint(0,20)
    ADS_innerlinethick = random.randint(0,10)
    ADS_innerlineoffset = random.randint(0,20)
    ADS_innerlinemovmenterr = random.randint(0,1)
    ADS_innerlinemovmentmultiply = float("{0:.3f}".format(random.uniform(0, 3)))
    ADS_innerlinefireerror = random.randint(0,1)
    ADS_innerlinefireerrormultiply = float("{0:.3f}".format(random.uniform(0, 3)))
    ADS_outerline = 1
    ADS_outerlineocap = float("{0:.3f}".format(random.uniform(0, 1)))
    ADS_outerlinelen = random.randint(0,20)
    ADS_outerlinelen2 = random.randint(0,20)
    ADS_outerlinethick = random.randint(0,10)
    ADS_outerlineoffset = random.randint(0,20)
    ADS_outerlinemovementerr = random.randint(0,1)
    ADS_outerlinemovementerrval= float("{0:.3f}".format(random.uniform(0, 3)))
    ADS_outterlinefiringeror = random.randint(0,1)
    ADS_outerlinefirringerrmultiply = float("{0:.3f}".format(random.uniform(0, 3)))
    S_color = ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    S_thick = float("{0:.3f}".format(random.uniform(0, 4)))
    S_ocap = float("{0:.3f}".format(random.uniform(0, 1)))
    crosshair = f'0;p;0;s;1;P;c;8;u;{color};h;{outline};t;{outlinethickness};o;{outlineocap};d;{dot};z;{dotsize};0b;{innerline};0a;{innerlineocap};0l;{innerlinelen};0v;{innerlinelen2};0g;1;0t;{innerlinethick};0o;{innerlineoffset};0m;{innerlinemovmenterr};0s;{innerlinemovmentmultiply};0f;{innerlinefireerror};0e;{innerlinefireerrormultiply};1b;{outerline};1a;{outerlineocap};1l;{outerlinelen};1v;{outerlinelen2};1g;1;1t;{outerlinethick};1o;{outerlineoffset};1m;{outerlinemovementerr};1s;{outerlinemovementerrval};1f;{outterlinefiringeror};1e;{outerlinefirringerrmultiply};A;c;8;u;{ADS_color};h;{ADS_outline};t;{ADS_outlinethickness};o;{ADS_outlineocap};d;{ADS_dot};z;{ADS_dotsize};0b;{ADS_innerline};0a;{ADS_innerlineocap};0l;{ADS_innerlinelen};0v;{ADS_innerlinelen2};0g;1;0t;{ADS_innerlinethick};0o;{ADS_innerlineoffset};0m;{ADS_innerlinemovmenterr};0s;{ADS_innerlinemovmentmultiply};0f;{ADS_innerlinefireerror};0e;{ADS_innerlinefireerrormultiply};1b;{ADS_outerline};1a;{ADS_outerlineocap};1l;{ADS_outerlinelen};1v;{ADS_outerlinelen2};1g;1;1t;{ADS_outerlinethick};1o;{ADS_outerlineoffset};1m;{ADS_outerlinemovementerr};1s;{ADS_outerlinemovementerrval};1f;{ADS_outterlinefiringeror};1e;{ADS_outerlinefirringerrmultiply};S;c;8;t;{S_color};s;{S_thick};o;{S_ocap}'
    return crosshair

if __name__ == '__main__':
    pyperclip.copy(crosshairgen())
    print("Crosshair have been copied to clipboard.")
