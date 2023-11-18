#include <cs50.h>

#include <stdio.h>

#include <string.h>
 // Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct {
  int winner;
  int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[]) {
  // Check for invalid usage
  if (argc < 2) {
    printf("Usage: tideman [candidate ...]\n");
    return 1;
  }

  // Populate array of candidates
  candidate_count = argc - 1;
  if (candidate_count > MAX) {
    printf("Maximum number of candidates is %i\n", MAX);
    return 2;
  }
  for (int i = 0; i < candidate_count; i++) {
    candidates[i] = argv[i + 1];
  }

  // Clear graph of locked in pairs
  for (int i = 0; i < candidate_count; i++) {
    for (int j = 0; j < candidate_count; j++) {
      locked[i][j] = false;
    }
  }

  pair_count = 0;
  int voter_count = get_int("Number of voters: ");

  // Query for votes
  for (int i = 0; i < voter_count; i++) {
    // ranks[i] is voter's ith preference
    int ranks[candidate_count];

    // Query for each rank
    for (int j = 0; j < candidate_count; j++) {
      string name = get_string("Rank %i: ", j + 1);

      if (!vote(j, name, ranks)) {
        printf("Invalid vote.\n");
        return 3;
      }
    }

    record_preferences(ranks);

    printf("\n");
  }

  add_pairs();
  sort_pairs();
  lock_pairs();
  print_winner();
  return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[]) {
  // TODO
  for (int i = 0; i < candidate_count; i++) {
    if (strcmp(name, candidates[i]) == 0) {
      ranks[rank] = i;
      return true;
    }
  }
  return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[]) {
  // TODO

  for (int i = 0; i < candidate_count; i++)

  {
    for (int j = i + 1; j < candidate_count; j++) {
      int first = ranks[i];
      int second = ranks[j];

      if (first != second) {
        preferences[first][second]++;
      } else {
        preferences[first][second] = 0;
      }
    }
  }
  return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)

// TODO
{
  for (int i = 0; i < candidate_count; i++)

  {
    for (int j = i + 1; j < candidate_count; j++) {
      int cmp1 = preferences[i][j];
      int cmp2 = preferences[j][i];
      if (cmp1 > cmp2) {
        pairs[pair_count].winner = i;
        pairs[pair_count].loser = j;
        pair_count++;
      } else if (cmp2 > cmp1) {

        pairs[pair_count].winner = j;
        pairs[pair_count].loser = i;
        pair_count++;
      }
    }
  }
  return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void) {
    // TODO
    for (int i = 0; i < pair_count; i++) {
        for (int j = 0; j < pair_count - i - 1; j++) {
            int i1 = pairs[j].winner;
            int j1 = pairs[j].loser;
            int st_pair1 = preferences[i1][j1] - preferences[j1][i1];

            int i2 = pairs[j + 1].winner;
            int j2 = pairs[j + 1].loser;
            int st_pair2 = preferences[i2][j2] - preferences[j2][i2];

            // Swap pairs if the strength of victory is greater for the second pair
            if (st_pair2 > st_pair1) {
                // Swap pairs
                pair temp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = temp;
            }
        }
    }
}
// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void) {
    // TODO: Implement the logic to lock pairs
    for (int i = 0; i < pair_count; i++) {
        int winner = pairs[i].winner;
        int loser = pairs[i].loser;

        // Check if adding this pair would create a cycle
        if (!creates_cycle(winner, loser)) {
            // Lock the pair
            locked[winner][loser] = true;
        }
    }
}

// Print the winner of the election
void print_winner(void) {
    // TODO: Implement the logic to print the winner
    for (int i = 0; i < candidate_count; i++) {
        bool is_winner = true;

        // Check if candidate i is the winner
        for (int j = 0; j < candidate_count; j++) {
            if (locked[j][i]) {
                is_winner = false;
                break;
            }
        }

        // If no one points to candidate i, print them as the winner
        if (is_winner) {
            printf("%s\n", candidates[i]);
            return;
        }
    }
}

