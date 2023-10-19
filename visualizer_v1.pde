import ddf.minim.*;
import ddf.minim.analysis.*;

Minim minim;
AudioInput in;
FFT fft;
float circleSize = 30;
float targetSize = circleSize;
float minSize = 30;
float maxSize = 100;
float smoothingFactor = 0.1;
color currentColor;
color targetColor;
boolean transitioningColor = false;
float amplitudeFactor = 1.0;
float glowRadius = 50;
color backgroundColor;
color targetBackgroundColor;
boolean transitioningBackgroundColor = false;

ArrayList<Particle> particles = new ArrayList<Particle>();

void setup() {
  size(800, 800);
  minim = new Minim(this);
  in = minim.getLineIn(Minim.STEREO);
  fft = new FFT(in.bufferSize(), in.sampleRate());
  noStroke();
  ellipseMode(CENTER);
  currentColor = color(255, 0, 0);
  targetColor = currentColor;
}

void draw() {
  background(0);
  fft.forward(in.mix);

  float trebleAmplitude = fft.getBand(6);
  targetBackgroundColor = color(map(trebleAmplitude, 0, 1, 0, 255), 255, 0);
  
  if (transitioningBackgroundColor) {
    backgroundColor = lerpColor(backgroundColor, targetBackgroundColor, 0.1);
    if (red(backgroundColor) == red(targetBackgroundColor) &&
        green(backgroundColor) == green(targetBackgroundColor) &&
        blue(backgroundColor) == blue(targetBackgroundColor)) {
      transitioningBackgroundColor = false;
    }
  }

  background(backgroundColor);

  float bassAmplitude = fft.getBand(2);
  targetSize = map(bassAmplitude * amplitudeFactor, 0, 1, minSize, maxSize);
  circleSize = lerp(circleSize, targetSize, smoothingFactor);

  if (transitioningColor) {
    currentColor = lerpColor(currentColor, targetColor, 0.1);
    if (red(currentColor) == red(targetColor) && green(currentColor) == green(targetColor) && blue(currentColor) == blue(targetColor)) {
      transitioningColor = false;
    }
  }

  for (int i = 0; i < glowRadius; i++) {
    float alpha = map(i, 0, glowRadius, 100, 0);
    fill(red(currentColor), green(currentColor), blue(currentColor), alpha);
    ellipse(width / 2, height / 2, circleSize + i, circleSize + i);
  }

  fill(currentColor);
  ellipse(width / 2, height / 2, circleSize, circleSize);

  // Update and display particles
  for (int i = particles.size() - 1; i >= 0; i--) {
    Particle p = particles.get(i);
    p.update();
    p.display();
    if (p.isDead()) {
      particles.remove(i);
    }
  }

  // Add new particles randomly
  if (random(1) < 0.1) {
    float px = random(width);
    float py = random(height);
    color pColor = color(random(255), random(255), random(255));
    particles.add(new Particle(px, py, pColor));
  }

  stroke(0);
  noFill();
  beginShape();
  for (int i = 0; i < in.bufferSize() - 1; i++) {
    float x1 = map(i, 0, in.bufferSize(), 0, width);
    float x2 = map(i + 1, 0, in.bufferSize(), 0, width);
    float y1 = height / 2 + in.left.get(i) * 200;
    float y2 = height / 2 + in.left.get(i + 1) * 200;
    line(x1, y1, x2, y2);
  }
}

void keyPressed() {
  if (key == 'c' || key == 'C') {
    targetColor = color(random(255), random(255), random(255));
    transitioningColor = true;
  } else if (key == 'j' || key == 'J') {
    amplitudeFactor -= 0.05;
    amplitudeFactor = max(amplitudeFactor, 0.0001);
    System.out.println(circleSize);
  } else if (key == 'k' || key == 'K') {
    amplitudeFactor += 0.05;
    amplitudeFactor = min(amplitudeFactor, 2.0);
      System.out.println(circleSize);
  } else if (key == 'b' || key == 'B') {
    targetBackgroundColor = color(random(255), random(255), random(255));
    transitioningBackgroundColor = true;
  }
}

class Particle {
  float x, y;
  PVector velocity;
  color pColor;
  
  Particle(float x, float y, color pColor) {
    this.x = x;
    this.y = y;
    this.velocity = PVector.random2D().mult(random(1, 4));
    this.pColor = pColor;
  }
  
  void update() {
    x += velocity.x;
    y += velocity.y;
    if (x < 0 || x > width || y < 0 || y > height) {
      // Wrap around when particles go off-screen
      x = (x + width) % width;
      y = (y + height) % height;
    }
  }
  
  void display() {
    noStroke();
    fill(pColor);
    ellipse(x, y, 5, 5);
  }
  
  boolean isDead() {
    // Particles "die" when they fade away
    return alpha(pColor) <= 0;
  }
}
