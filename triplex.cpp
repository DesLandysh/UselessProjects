#include <iostream>
#include <ctime>

// void shows the foo don't return anything
void PrintIntro(int Difficulty)
{
    // Print welcome messages to the terminal
    std::cout <<
"\n    _____"
"\n   /    /|_ ___________________________________________"
"\n  /    // /|                                          /|"
"\n (====|/ //   You are elf bookkeeper...    _QP_      / |"
"\n  (=====|/  and managing Santa's finances (  ' )    / .|"
"\n (====|/                                   \\__/    / /||"
"\n/_________________________________________________/ / ||"
"\n|  _____________________________________________  ||  ||"
"\n| ||                                            | ||"
"\n| ||                                            | ||"
"\n| |                                             | |\n\n"
"You have to guess how many children lived in the house #" << Difficulty;
"\nby counting of dropped gifts.\n"
"Enter the number of children in every of three rooms...\n";
}

bool PlayGame(int Difficulty)
{
    PrintIntro(Difficulty);
    
    // Declare 3 number code
    // pure rand() returns a number between 0 and 32767
    const int ChildrenInRoomA = rand() % Difficulty + Difficulty;
    const int ChildrenInRoomB = rand() % Difficulty + Difficulty;
    const int ChildrenInRoomC = rand() % Difficulty + Difficulty;

    const int SumOfGifts = ChildrenInRoomA + ChildrenInRoomB + ChildrenInRoomC;
    const int ProductOfGifts = ChildrenInRoomA * ChildrenInRoomB * ChildrenInRoomC;

    // Print sum and product to the terminal
    std::cout << "\nThere are 3 rooms where children live.\n";
    std::cout << "> " << SumOfGifts << " is the sum of dropped gifts by Santa, one for each child.\n";
    std::cout << "> " << ProductOfGifts << " is the product of dropped gifts.\n";

    // Declare and get the User's input
    int GuessA, GuessB, GuessC, GuessSum, GuessProduct;
    std::cin >> GuessA >> GuessB >> GuessC;

    GuessSum = GuessA + GuessB + GuessC;
    GuessProduct = GuessA * GuessB * GuessC;
    
    //Debugging lines
    //std::cout << ChildrenInRoomA << ChildrenInRoomB << ChildrenInRoomC;
    //std::cout << "\nYou entered: " << GuessA << GuessB << GuessC;
    //std::cout << "\n" << GuessSum << " is your sum, and your product is: " << GuessProduct;

    // Check if the user's guess right
    if (GuessSum == SumOfGifts && GuessProduct == ProductOfGifts)
    {
        std::cout << "\n*** You win! Next Year Santa's budget will be bigger. ***";
        return true;
    }
    else
    {
        std::cout << "\n*** Try again, if you don't want to be fired after incorrect economic machinations. ***";
        return false;
    }

}

int main()
{
    srand(time(NULL)); // create new random sequence based on time of day
    int LevelDifficulty = 1;
    const int MaxLevel = 5;

    while (LevelDifficulty <= MaxLevel)
    {
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear(); // clears any errors
        std::cin.ignore(); // clean buffer

        if (bLevelComplete)
        {
            ++LevelDifficulty;
        }
    }

    std::cout << "\n*** Great work elf! You got all the houses! Now you you have a chance to get bonus payment. ***";
    return 0;
}