class Eff1:
    def __init__(self):
        self.scale = 20
        self.colorR=0.5
        self.colorG=0.8
    
    def modOne(self, delta):
        self.scale += delta

    def modTwo(self, delta):
        self.colorR += delta*.1
    
    def modThree(self, delta):
        self.colorG += delta*.1

    def getFinalCommand(self):
        finalCmd = f'shape(20,0.2,0.3).color({self.colorR},{self.colorG},50).scale(() => Math.sin(time)+1*2).repeat(() => Math.sin(time)*{self.scale}).modulateRotate(o0).scale(() => Math.sin(time)+1 *1.5).modulate(noise(2,2)).rotate(1, .2).out(o0)'
        return finalCmd

class Eff2:
    def __init__(self):
        self.colorR=1.01
        self.colorG=1.01
        self.colorB=1.01
    
    def modOne(self, delta):
        self.colorR += delta*.1

    def modTwo(self, delta):
        self.colorG += delta*.1
    
    def modThree(self, delta):
        self.colorB += delta*.1

    def getFinalCommand(self):
        finalCmd = f"src(o0).saturate(1.01).scale(.999).color({self.colorR},{self.colorG},{self.colorB}).hue(.01).modulateHue(src(o1).hue(.3).posterize(-1).contrast(.7),2).layer(src(o1).luma().mult(gradient(1).saturate(.9))).out(o0)\nnoise(1, .2).rotate(2,.5).layer(src(o0).scrollX(.2)).out(o1)\nrender(o0)"
        return finalCmd

class Eff3:
    def __init__(self):
        self.voronoi=5
        self.osc=1
        self.scale=1
    
    def modOne(self, delta):
        self.voronoi += delta

    def modTwo(self, delta):
        self.osc += delta*.1
    
    def modThree(self, delta):
        self.scale += delta*.1

    def getFinalCommand(self):
        finalCmd=f'voronoi({self.voronoi},-0.1,1).add(osc(1,{self.osc},1)).kaleid(21).scale({self.scale},1,2).colorama().out(o1)\nsrc(o1).mult(src(s0).modulateRotate(o1,100), -0.5).out(o0)'
        return finalCmd

class Eff4:
    def __init__(self):
        self.osc=10
        self.color=1
        self.repeat=2
    
    def modOne(self, delta):
        self.osc += delta

    def modTwo(self, delta):
        self.color += delta*.1
    
    def modThree(self, delta):
        self.repeat += delta*.1

    def getFinalCommand(self):
        finalCmd = f"osc({self.osc}, 1, 0).color(2, {self.color}, 2).mult(osc(20, 0.01, 0)).repeat({self.repeat}, 20).rotate(0.5).modulate(o1).scale(1, () =>  (a.fft[0]*0.9 + 2)).diff(o1).out(o0)\nosc(20, 0.2, 0).color(2, 0.7, 0.1).mult(osc(40)).modulateRotate(o0, 0.2).rotate(0.2).out(o1)"
        return finalCmd
    
class Eff5:
    def __init__(self):
        self.bright=1.2
        self.shape=20
        self.shapeScale=0.5
    
    def modOne(self, delta):
        self.bright += delta*.1

    def modTwo(self, delta):
        self.shape += delta
    
    def modThree(self, delta):
        self.shapeScale += delta*.1

    def getFinalCommand(self):
        finalCmd = f"noise(6,.05).mult( osc(9,0, ()=>Math.sin(time/1.5)+2 ) ).mult(noise(9,.03).brightness({self.bright}).contrast(2).mult( osc(9,0, ()=>Math.sin(time/3)+13 ) )).diff(noise(15,.04).brightness(.2).contrast(1.3).mult( osc(9,0, ()=>Math.sin(time/5)+13 ) ).rotate( ()=>time/33 )).scale( ()=>Math.sin(time/6.2)*.12+.15 ).modulateScale(osc(3,0,0).mult( osc(3,0,0).rotate(3.14/2) ).rotate( ()=>time/25 ).scale(.39).scale(1,.6,1).invert(), ()=>Math.sin(time/5.3)*1.5+3  ).rotate( ()=>time/22 ).mult( shape({self.shape},{self.shapeScale},.01).scale(1,.6,1) ).out()"
        return finalCmd

class Eff6:
    def __init__(self):
        self.osc1=10
        self.osc2=.001
        self.scale = 0.8
    
    def modOne(self, delta):
        self.osc1 += delta

    def modTwo(self, delta):
        self.osc2 += delta*.01
    
    def modThree(self, delta):
        self.scale += delta*.1

    def getFinalCommand(self):
        finalCmd = f'osc(9, 0.03, 1.7).kaleid().mult(osc({self.osc1}, {self.osc2}, 0).rotate(1.58)).blend(o0, 0.94).modulateScale(osc(10, 0),-0.03).scale({self.scale}, () => (1.05 + 0.1 * Math.sin(0.05*time))).out(o0)'
        return finalCmd

class Eff7:
    def __init__(self):
        self.osc=10
        self.color=1
        self.color2=2
    
    def modOne(self, delta):
        self.osc += delta

    def modTwo(self, delta):
        self.color += delta*.1
    
    def modThree(self, delta):
        self.color2 += delta*.1

    def getFinalCommand(self):
        finalCmd = f"osc(105).color(0.5,0.1,{self.color2}).rotate(0.5, 0.1).modulate(osc({self.osc}).rotate(0.3).add(o0, 0.1)).add(osc(20,0.01,1).color(0,0.8,1)).out(o0)\nosc(50,0.05, 0.7).color({self.color},0.7,0.5).diff(o0).modulate(o1,0.05).out(o1)\nrender(o1)"
        return finalCmd

class Eff8:
    def __init__(self):
        self.repeatX=2
        self.repeatY=2
        self.color=1
    
    def modOne(self, delta):
        self.osc += delta

    def modTwo(self, delta):
        self.color += delta*.1
    
    def modThree(self, delta):
        self.color2 += delta*.1

    def getFinalCommand(self):
        finalCmd = f"osc( 215, 0.1, 2 ).modulate(osc( 2, -0.3, 100 ).rotate(15)).mult(osc( 215, -0.1, 2).pixelate( 50, 50 )).color( .1, 0.0, 0.9 ).modulate(osc( 6, -0.1 ).rotate( 9 )).add(osc( 10, -0.9, 900 ).color(1,{self.color},1)).mult(shape(900, 0.2, 1).luma().repeatX({self.repeatX}).repeatY({self.repeatY}).colorama(10)).modulate(osc( 9, -0.3, 900 ).rotate( 6 )).add(osc(4, 1, 90).color(0.2,0,1)).out()"
        return finalCmd
    
class Eff9:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = f"n = 8\na = () => shape(4,0.25,0.009).rotate(()=>time/-40).repeat(n,n)\na().add(a().scrollX(0.5/n).scrollY(0.5/n),1).modulate(o1,{self.modulate}).modulate(src(o1).color(10,10).add(solid(-14,-14)).rotate(()=>time/40),0.005).add(src(o1).scrollY(0.012,0.02),0.5).out(o1)\nsrc(o1).colorama(1.2).posterize(4).saturate(0.7).contrast(6).mult(solid(),0.15).out(o0)"
        return finalCmd
    
class Eff10:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'noise(18).colorama(1).posterize(2).kaleid(50).mask(shape(25, 0.25).modulateScale(noise(400.5, 0.5))).mask(shape(400, 1, 2.125)).modulateScale(osc(6, 0.125, 0.05).kaleid(50)).mult(osc(20, 0.05, 2.4).kaleid(50), 0.25).scale(1.75, 0.65, 0.5).modulate(noise(0.5)).saturate(6).posterize(4, 0.2).scale(1.5).out()'
        return finalCmd

class Eff11:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'osc(7,-0.125).modulate(voronoi(1)).diff(voronoi(1).mult(gradient(-1).luma(0.125))).luma(0.125).add(shape(7, 0.5).mult(voronoi(10,2).blend(o0).diff(gradient(1)).modulate(voronoi()))).scrollY(-0.1).scrollX(0.125).blend(o0).blend(o0).out()'
        return finalCmd
    
class Eff12:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'osc(10, 0.9, 300).color(0.9, 0.7, 0.8).diff(osc(45, 0.3, 100).color(0.9, 0.9, 0.9).rotate(0.18).pixelate(12).kaleid()).scrollX(10).colorama().luma().repeatX(4).repeatY(4).modulate(osc(1, -0.9, 300)).scale(2).out()'
        return finalCmd
    
class Eff13:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'osc(100, 0.01, 1.4).rotate(0, 0.1).mult(osc(10, 0.1).modulate(osc(10).rotate(0, -0.1), 1)).color(2.83,0.91,0.39).out(o0)'
        return finalCmd
    
class Eff14:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'voronoi(8,1).mult(osc(10,0.1,()=>Math.sin(time)*3).saturate(3).kaleid(200)).modulate(o0,0.5).add(o0,0.8).scrollY(-0.01).scale(0.99).modulate(voronoi(8,1),0.008).luma(0.3).out()'
        return finalCmd
    
class Eff15:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'osc(3, 0.01, 0.4).color(1.2,1.2,1.3).saturate(0.4).modulateRepeat(osc(2),1, 2, 4, 3).modulateKaleid(osc(12,0.05,0),1).luma (0.4).rotate(4, 0.1,0).modulate(o0, () => mouse.y *0.0002 ).scale(1).diff(o1).out(o0)'
        return finalCmd
    
class Eff16:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'voronoi(2,0.3,0.2).shift(0.5).modulatePixelate(voronoi(4,0.2),32,2).scale(()=>1+(Math.sin(time*2.5)*0.05)).diff(voronoi(3).shift(0.6)).diff(osc(2,0.15,1.1).rotate()).brightness(0.1).contrast(1.2).saturate(1.2).out()'
        return finalCmd
    
class Eff17:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'osc(40,0.2,1).modulateScale(osc(40,0,1).kaleid(8)).repeat(2,4).modulate(o0,0.05).modulateKaleid(shape(4,0.1,1)).out(o0)'
        return finalCmd

class Eff18:
    def __init__(self):
        self.colorama=1.4
        self.posterize=4
        self.modulate=.5
    
    def modOne(self, delta):
        self.colorama += delta*.1

    def modTwo(self, delta):
        self.posterize += delta
    
    def modThree(self, delta):
        self.modulate += delta*.1

    def getFinalCommand(self):
        finalCmd = 'gradient(0.25).add(noise(), ()=>Math.cos(time)).modulateRotate(src(o0).rotate(0, -0.52), 0.2).mult(shape(360), 0.8).repeat(10,5).mult(shape(360).scale(()=>Math.sin(time)), 0.8).rotate(0, 0.2).diff(src(o0).rotate(0, -0.2), 0.2).out()'
        return finalCmd