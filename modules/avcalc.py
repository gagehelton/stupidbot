import math

cd = [49,50,55,65,70,75,82,85,86,98]
aspect_ratio = math.sqrt((16/9)**2+1)
common_sizes = {24.02280074199539: 49, 
                24.51306198162795: 50, 
                26.964368179790743: 55, 
                31.866980576116333: 65, 
                34.31828677427913: 70, 
                36.76959297244192: 75, 
                40.201421649869836: 82, 
                41.672205368767514: 85, 
                42.162466608400074: 86, 
                48.04560148399078: 98}
                
#4/6/8 display sizing rule
class fourSixEight():

    def get_height(diagonal):
        return diagonal/aspect_ratio

    #fv(furthest viewer) in feet
    def get_display_size(fv):
        f = fv
        fv=fv*12
        def closest(div):
            margin = 6
            if(fv/div > (list(common_sizes)[-1]+margin)):
                return ["Uncommon Display / Projector Screen",'Display @ {}" height'.format(fv/div)]
            return ["Common Display",str(common_sizes.get(float(fv/div), 
                                        common_sizes[min(common_sizes.keys(), 
                                        key=lambda k: abs(k-float(fv/div)))]))+'" Display']
        return {"feet":f,"four":closest(4),"six":closest(6),"eight":closest(8)}

def mm2in(args):
    if(not isinstance(args,list)):
        return False
    _MM = args[0].strip().replace(" ","").lower().split("x")
    _IN = []
    try:
        _PLACES = int(args[1])
    except IndexError:
        _PLACES = 100
    if(isinstance(_MM,list)):
        for i in range(len(_MM)):
            _IN.append(round(float(_MM[i])*0.0394,_PLACES))
        return {"_MM":"x".join([str(i) for i in _MM]),"_IN":"x".join([str(i) for i in _IN])}
    return False    

if __name__ == '__main__':
    print(mm2in(['1200x1000x100']))
    
