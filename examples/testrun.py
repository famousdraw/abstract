print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
import sys
import inference
def test():
    embs,sen=inference.prepare_embs()
    rel=inference.inference_from_embs(embs,sen)
    y_=inference.knn_treat(rel)
    return(inference.inference_after_knn(y_,sen))
if __name__ == '__main__':
    print ('作为主程序运行')
    import os
    print('testrun.py')
    print('当前目录为：',os.getcwd())
    os.chdir("..")
    print(os.getcwd( ))
    import sys
    sys.path.append("..\src")
    sys.path.append("..\data")
    sys.path.append('..\examples')
    print(sys.path)
    import pre_proc
    print(test())

else:
    print("package_testrun 初始化")