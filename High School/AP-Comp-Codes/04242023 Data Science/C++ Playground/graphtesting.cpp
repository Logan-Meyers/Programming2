#include <iostream>
#include <random>
#include <unistd.h>


void plotGraph(FILE* gp, std::vector<double> xVals, std::vector<double> yVals) {
    // initial 'tell gnuplot to accept x-y values'
    fprintf(gp, "plot '-' with lines\n");

    // string for formatting x and y val data
    const char* formatString = "%f %f\n";

    // loop to plot values
    for (int xIndex = 0; xIndex < xVals.size()-1; xIndex++) {
        fprintf(gp, formatString, xVals[xIndex], yVals[xIndex]);
    }

    // final 'e' for end, gnuplot will graph points, connected by a line
    fprintf(gp, "e\n");
}

std::vector<double> makeRandomList(int arraySize, int minVal = -100000, int maxVal = 100000) {
    // some random setup stuff
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(minVal, maxVal); // generate integers between min and max

    // the list to add values to
    std::vector<double> randomList;

    // generate and add values to list
    for (int i = 0; i < arraySize; ++i) {
        randomList.push_back(dist(gen));
    }

    // return list
    return randomList;
}

int main() {
    // open pipe to gnuplot
    FILE *gp = popen("gnuplot -persist", "w");

    if (gp == NULL) {
        std::cout << "Error opening pipe to gnuplot\n";
        return -1;
    }

    // set up graph titles and such
    fprintf(gp, "set title 'sin(x)'\n");
    fprintf(gp, "set xlabel 'x'\n");
    fprintf(gp, "set ylabel 'sin(x)'\n");

    for (int bigloop = 0; bigloop < 50; bigloop++) {
        std::vector<double> xVals;
        std::vector<double> yVals = makeRandomList(100, -10, 10);

        for (int x = 0; x < yVals.size(); x++) {
            xVals.push_back(x);
        }

        plotGraph(gp, xVals, yVals);

        std::cout << "Plotted graph, with bigloop at: " << bigloop << "\n";
        usleep(1000000);
    }

    // close gnuplot and return
    pclose(gp);
    return 0;
}

// http://gnuplot.info/docs_5.5/gnuplot5.html