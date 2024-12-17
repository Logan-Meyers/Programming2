#include <stdio.h>
#include <stdlib.h>

#define NUM_REPORTS 1000
#define SRC_FILE "reports.txt"

int main() {
    // init variables
    int levels[NUM_REPORTS] = {};
    int safe_reports = 0;

    FILE *lvl_counter = fopen(SRC_FILE, "r");  // to count levels from

    for (int report = 0; report < NUM_REPORTS; report++) {
        int lvls_for_report = 1;

        while (1) {
            char curr;
            fscanf(lvl_counter, "%c", &curr);

            // break if newline found or file ended
            if (curr == '\n') break;
            if (feof(lvl_counter)) break;

            // increment levels if space found
            if (curr == ' ') lvls_for_report++;
        }

        // add to list
        levels[report] = lvls_for_report;
    }

    // close file for level reading, open new file for report reading
    fclose(lvl_counter);
    FILE *reports = fopen(SRC_FILE, "r");

    // parse by report line num
    for (int report=0; report < NUM_REPORTS; report++) {
        int last = 0, current = 0, direction = 0;
        int valid = 1;

        // read first num, set to 'current'
        fscanf(reports, "%d", &current);

        // loop at most the corresponding number of levels
        for (int level=1; level < levels[report]; level++) {
            if (valid) {
                // read and swap last and current values
                last = current;
                fscanf(reports, "%d", &current);

                // determine invalid step amount (< 1 or > 3)
                int diff = last - current;
                if (abs(diff) < 1 || abs(diff) > 3) { 
                    printf("report %d invalid\n", report);
                    valid = 0;
                    continue;
                }

                // determine new direction
                int curr_dir = 0;
                if (last < current) curr_dir = 1;
                else if (last > current) curr_dir = -1;

                // set main direction if needed
                if (direction == 0) direction = curr_dir;
                // otherwise determine if directions are different
                else if (direction != curr_dir) {
                    printf("Report %d change direction at level %d\n", report, level);
                    valid = 0;
                    continue;
                }
            } else {
                // just read a number to get to the next line
                int tmp;
                fscanf(reports, "%d", &tmp);
                printf("Read %d to get to the next line\n", tmp);
            }
        }

        // if report is safe, increment
        if (valid) {
            safe_reports++;
            printf("Report %d is safe\n", report);
        }
    }

    printf("Safe reports: %d\n", safe_reports);
}