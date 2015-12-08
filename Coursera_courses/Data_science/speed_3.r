# Initialize the speed variable
speed <- 79

while(speed > 30) {
  print(paste("Your speed is",speed))
  
  # Break the while loop when speed exceeds 80
  
  
  if(speed >= 80) {
    break
  }    
    else if (speed > 48& speed < 80) {
    print("Slow down big time!")
    speed <- speed - 11
  } else {
    print("Slow down!")
    speed <- speed - 6
  }
}