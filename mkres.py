#! /usr/bin/python
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-E", "--edu",    help="Include Education",   action="store_true")
    parser.add_argument("-p", "--pomona", help="Dont Include Pomona", action="store_false")
    parser.add_argument("-a", "--isa",    help="Dont Include ISA",    action="store_false")

    parser.add_argument("-R", "--rsch",   help="Include Research",    action="store_true")
    parser.add_argument("-t", "--thesis", help="Dont Include Thesis", action="store_false")
    parser.add_argument("-s", "--iso",    help="Dont Include Iso",    action="store_false")
    parser.add_argument("-i", "--imies",  help="Dont Include imies",  action="store_false")
    parser.add_argument("-h", "--paths",  help="Dont Include paths",  action="store_false")
    parser.add_argument("-g", "--github", help="Dont Include github", action="store_false")

    parser.add_argument("-X", "--exp",    help="Include Experience",     action="store_true")
    parser.add_argument("-o", "--orig",   help="Dont Include Originate", action="store_false")
    parser.add_argument("-A", "--assist", help="Dont include TA",        action="store_false")
    parser.add_argument("-c", "--tfac",   help="Dont Include TFAC",      action="store_false")
    parser.add_argument("-l", "-ios",     help="Dont Include IpadApp",   action="store_false")
    
    parser.add_argument("-T", "--teach", help="Include Teaching", action="store_true")

    parser.add_argument("-P", "--proj",      help="Include Projects",       action="store_true")
    parser.add_argument("-m", "--mathswipe", help="Dont Include Mathswipe", action="store_false")
    parser.add_argument("-r", "--roomdraw",  help="Dont Include RoomDraw",  action="store_false")
    parser.add_argument("-e", "--grademail", help="Dont Include gradEmail", action="store_false")    
    parser.add_argument("-S", "--semantics", help="Dont Include semantics", action="store_false")
    
    parser.add_argument("-C", "-extra", help="Include Extracurrics", action="store_true")
    
    args = parser.parse_args()

    

    
if __name__ == "__main__" : main()
