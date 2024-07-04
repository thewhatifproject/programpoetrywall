// Title: Code of Perseverance
// Powered by The 'What If' Project
// Generated and wrote by: Daniele G

include <iostream>
using namespace std;

// Main function to persevere
int main() {
    // Define variables of hope and strength
    int hope = 100;
    int strength = 100;

    // While loop to represent the journey
    while (hope > 0 && strength > 0) {
        // Output the ongoing effort
        cout << "Keep pushing forward, never cease!" << endl;

        // Deduct some hope and strength, simulating challenges
        hope -= 10;
        strength -= 10;

        // Conditional statement to add determination
        if (hope < 50) {
            cout << "Hope is low, but determination rises!" << endl;
            strength += 20;
        }
    }

    // Final message of success
    cout << "Through trials and tribulations, we succeed!" << endl;

    return 0;
}