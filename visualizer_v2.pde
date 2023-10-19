import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

Minim minim;
AudioInput in;
FFT fft;

int numCircles = 10;
float speedMultiplier = 1.0;
Circle[] circles;

void setup() {
  size(800, 600);
  minim = new Minim(this);
  in = minim.getLineIn(Minim.STEREO, 512);
  fft = new FFT(in.bufferSize(), in.sampleRate());
  
  circles = new Circle[numCircles];
  for (int i = 0; i < numCircles; i++) {
    circles[i] = new Circle(random(width), random(height), random(20, 40));
  }
}

void draw() {
  background(0);

  fft.forward(in.mix);

  for (int i = 0; i < numCircles; i++) {
    Circle circle = circles[i];
    circle.update(speedMultiplier); // Pass the speedMultiplier to the update method
    circle.display();
  }
}


class Circle {
  float x, y;
  float radius;
  float xSpeed, ySpeed;
  
  Circle(float x, float y, float radius) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    xSpeed = random(2, 4);
    ySpeed = random(2, 4);
  }
  
void update(float speedMultiplier) {
  x += xSpeed * speedMultiplier; // Adjust speed with the multiplier
  y += ySpeed * speedMultiplier;

  // Check for collisions with the window borders
  if (x - radius < 0 || x + radius > width) {
    xSpeed *= -1;
  }
  if (y - radius < 0 || y + radius > height) {
    ySpeed *= -1;
  }

  // Adjust circle color based on the audio amplitude using HSB
  float amplitude = fft.getBand(1); // Adjust the index for the desired frequency band
  float hue = map(amplitude, 0, 1, 0, 360); // Map amplitude to hue (0-360)
  float saturation = 100; // You can adjust this value for desired saturation
  float brightness = 100; // You can adjust this value for desired brightness
  fill(hue, saturation, brightness);
}

void keyPressed() {
  if (key == '-') {
    // Decrease speed when the "-" key is pressed
    speedMultiplier *= 0.9; // You can adjust the factor for the speed change
  } else if (key == '=') {
    // Increase speed when the "=" key is pressed
    speedMultiplier *= 1.1; // You can adjust the factor for the speed change
  }
}


  
  void display() {
    ellipse(x, y, radius * 2, radius * 2);
  }
}
