"""
A file named `init_unreal.py` placed in the UE5 Python path is executed immediately upon UE5 startup.
"""
import unreal

if __name__ == '__main__':
    unreal.log('The init_unreal script has been executed!')
