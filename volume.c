#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header (standard for PCM WAV files)
const int HEADER_SIZE = 44;

int main(int argc, char *argv[]) {
  // Check command-line arguments
  if (argc != 4) {
    printf("Usage: ./volume input.wav output.wav factor\n");
    return 1;
  }

  // Open files
  FILE *input = fopen(argv[1], "rb");
  if (input == NULL) {
    printf("Could not open input file.\n");
    return 1;
  }

  FILE *output = fopen(argv[2], "wb");
  if (output == NULL) {
    printf("Could not open output file.\n");
    fclose(input);
    return 1;
  }

  // Get scaling factor from command line argument
  float factor = atof(argv[3]);

  // Enforce a safe factor range to avoid clipping (distortion)
  if (factor <= 0.0f) {
    factor = 0.1f;  // Minimum positive factor to avoid zero-division
  } else if (factor > 5.0f) {
    factor = 5.0f;  // Maximum factor to avoid overflow
  }

  // Copy header from input to output file
  uint8_t header[HEADER_SIZE];
  if (fread(header, sizeof(uint8_t), HEADER_SIZE, input) != HEADER_SIZE) {
    printf("Error reading header.\n");
    fclose(input);
    fclose(output);
    return 1;
  }
  fwrite(header, sizeof(uint8_t), HEADER_SIZE, output);

  // Read samples from input, apply factor, and write to output
  int16_t buffer;
  while (fread(&buffer, sizeof(int16_t), 1, input)) {
    // Apply factor with a safe range for the data type (int16_t)
    int32_t temp = buffer * factor;  // Use temporary int32_t to avoid overflow
    if (temp > INT16_MAX) {
      buffer = INT16_MAX;
    } else if (temp < INT16_MIN) {
      buffer = INT16_MIN;
    } else {
      buffer = (int16_t)temp;  // Cast back to int16_t
    }
    fwrite(&buffer, sizeof(int16_t), 1, output);
  }

  // Close files
  fclose(input);
  fclose(output);
  return 0;
}
