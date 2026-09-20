"""

  This program demonstrates the Genetic Algorithm (GA) using a population of
  50 randomly generated members. Each member has biological traits that are
  evaluated for "fitness" in a simulated environment.

  GENETIC ALGORITHM FLOW :
  ┌─────────────────────────────────────────────────┐
  │  1. INITIALIZATION  — Generate random population│
  │          ↓                                      │
  │  2. EVALUATION      — Calculate fitness scores  │
  │          ↓                                      │
  │  3. SELECTION        — Pick the fittest (top 50%)│
  │          ↓           ← ─ ─ ─ ─ ─ ─ ─ ─ ┐      │
  │  4. RECOMBINATION   — Crossover parents  │      │
  │          ↓                               │      │
  │  5. MUTATION        — Random trait change │      │
  │          ↓                               │      │
  │  6. EVALUATION      — Re-evaluate fitness│      │
  │          ↓                               │      │
  │  7. TERMINAL?       — Loop back or stop ─┘      │
  │          ↓                                      │
  │  8. DISPLAY RESULT  — Show final ranked table   │
  └─────────────────────────────────────────────────┘

  Darwinian Concepts Demonstrated:
    * Survival of the Fittest  — Higher fitness → more likely to survive
    * Beneficial Traits        — Certain trait combos yield better fitness
    * Recombination            — Offspring inherit mixed traits from parents
    * Genetic Diversity        — Mutation introduces new trait variations

"""

import random

# ─────────────────────────────────────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

POPULATION_SIZE = 50          # Number of members in the population
NUM_GENERATIONS = 5           # Number of GA loop iterations
MUTATION_RATE = 0.2           # 20% chance a trait mutates
CROSSOVER_RATE = 0.7          # 70% chance parents undergo crossover

# Trait options for random generation
NAMES = [
    "Aarav", "Aditi", "Arjun", "Ananya", "Bharath", "Bhavya", "Charan", "Charvi",
    "Deepak", "Divya", "Eshan", "Eshwari", "Farhan", "Fathima", "Ganesh", "Gayathri",
    "Hari", "Harini", "Ishaan", "Ishwarya", "Jai", "Janani", "Karthik", "Kavya",
    "Lakshman", "Lakshmi", "Mohan", "Meera", "Naveen", "Nithya", "Om", "Oviya",
    "Pranav", "Priya", "Rahul", "Roshini", "Sanjay", "Shalini", "Tharun", "Thenmozhi",
    "Uday", "Uma", "Varun", "Vaishnavi", "Wasim", "Yazhini", "Yuvan", "Zara",
    "Abishek", "Aarthi"
]
GENDERS = ["Male", "Female"]
HEIGHT_RANGE = (140, 200)     # Height in cm
SKIN_COLOURS = ["Fair", "Wheatish", "Brown", "Dark", "Very Dark"]

# Ideal/beneficial trait values for fitness calculation
# (In this simulation, the "environment" favours these traits)
IDEAL_HEIGHT = 175            # Ideal height in cm
IDEAL_SKIN_INDEX = 2          # Index in SKIN_COLOURS (Brown = adapted to moderate UV)


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 1: INITIALIZATION — Create the initial random population
# ─────────────────────────────────────────────────────────────────────────────

def create_random_member(sno):
    """Generate one random member with biological traits."""
    return {
        "S.No": sno,
        "Name": random.choice(NAMES),
        "Gender": random.choice(GENDERS),
        "Height": random.randint(HEIGHT_RANGE[0], HEIGHT_RANGE[1]),
        "Skin Colour": random.choice(SKIN_COLOURS),
        "Recombination": "No",    # Will be updated during crossover
        "Mutation": "No",         # Will be updated during mutation
        "Fitness Score": 0.0      # Will be calculated during evaluation
    }


def initialize_population(size):
    """Create the initial population of random members."""
    print("\n" + "=" * 80)
    print("  STEP 1: INITIALIZATION — Generating random population of", size, "members")
    print("=" * 80)
    population = [create_random_member(i + 1) for i in range(size)]
    print(f"  ✓ {size} members generated with random traits.\n")
    return population


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 2 & 6: EVALUATION — Calculate fitness score for each member
# ─────────────────────────────────────────────────────────────────────────────

def calculate_fitness(member):
    """
    Calculate fitness score based on how close traits are to 'ideal' values.

    Fitness Score formula (out of 100):
      - Height score (max 50):  50 - |height - ideal_height|
      - Skin adaptation (max 30): 30 - (|skin_index - ideal_index| * 10)
      - Diversity bonus (max 20): Random genetic advantage

    This simulates natural selection where certain trait combinations
    give survival advantages in a specific environment.
    """
    # Height fitness: closer to ideal = higher score
    height_score = max(0, 50 - abs(member["Height"] - IDEAL_HEIGHT))

    # Skin colour adaptation: closer to ideal index = higher score
    skin_index = SKIN_COLOURS.index(member["Skin Colour"])
    skin_score = max(0, 30 - abs(skin_index - IDEAL_SKIN_INDEX) * 10)

    # Genetic diversity bonus (random inherent advantage)
    diversity_bonus = random.uniform(0, 20)

    fitness = round(height_score + skin_score + diversity_bonus, 2)
    return fitness


def evaluate_population(population, step_label="EVALUATION"):
    """Evaluate fitness scores for the entire population."""
    print(f"\n  STEP: {step_label} — Calculating fitness scores...")
    for member in population:
        member["Fitness Score"] = calculate_fitness(member)
    # Rank by fitness score (descending)
    population.sort(key=lambda m: m["Fitness Score"], reverse=True)
    # Reassign S.No based on rank
    for rank, member in enumerate(population, 1):
        member["S.No"] = rank
    print(f"  ✓ All {len(population)} members evaluated and ranked by fitness.\n")
    return population


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 3: SELECTION — Survival of the Fittest
# ─────────────────────────────────────────────────────────────────────────────

def selection(population):
    """
    Select the top 50% fittest individuals to be parents.
    This demonstrates SURVIVAL OF THE FITTEST — only the strongest survive
    to pass their genes to the next generation.
    """
    print("\n" + "-" * 80)
    print("  STEP 3: SELECTION — Survival of the Fittest")
    print("-" * 80)
    half = len(population) // 2
    selected = population[:half]  # Top 50% by fitness
    print(f"  ✓ Selected top {half} members (fittest survive).")
    print(f"  ✗ Bottom {len(population) - half} members eliminated (not fit enough).\n")
    print(f"  → Survivors: {', '.join(m['Name'] for m in selected[:5])}... and more\n")
    return selected


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 4: RECOMBINATION (Crossover) — Combining parent traits
# ─────────────────────────────────────────────────────────────────────────────

def recombination(parents, target_size):
    """
    Create offspring by combining traits of two parents (crossover).
    This demonstrates RECOMBINATION — offspring inherit a mix of traits
    from both parents, creating new trait combinations.
    """
    print("-" * 80)
    print("  STEP 4: RECOMBINATION — Crossover of parent traits")
    print("-" * 80)
    offspring = []
    crossover_count = 0

    while len(offspring) < target_size:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)

        child = {
            "S.No": 0,
            "Name": parent1["Name"] if random.random() < 0.5 else parent2["Name"],
            "Gender": random.choice(GENDERS),
            "Height": 0,
            "Skin Colour": "",
            "Recombination": "No",
            "Mutation": "No",
            "Fitness Score": 0.0
        }

        if random.random() < CROSSOVER_RATE:
            # Crossover: blend traits from both parents
            child["Height"] = (parent1["Height"] + parent2["Height"]) // 2
            child["Height"] += random.randint(-3, 3)  # slight variation
            child["Skin Colour"] = random.choice([parent1["Skin Colour"],
                                                   parent2["Skin Colour"]])
            child["Recombination"] = "Yes"
            crossover_count += 1
        else:
            # No crossover: child copies one parent entirely
            chosen_parent = random.choice([parent1, parent2])
            child["Height"] = chosen_parent["Height"]
            child["Skin Colour"] = chosen_parent["Skin Colour"]
            child["Recombination"] = "No"

        offspring.append(child)

    print(f"  ✓ {len(offspring)} offspring created.")
    print(f"  ✓ {crossover_count} underwent crossover (trait mixing).")
    print(f"  ✗ {len(offspring) - crossover_count} inherited single-parent traits.\n")
    return offspring


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 5: MUTATION — Random changes to introduce genetic diversity
# ─────────────────────────────────────────────────────────────────────────────

def mutation(population):
    """
    Randomly mutate traits in some members.
    This demonstrates GENETIC DIVERSITY — mutations introduce new variations
    that may be BENEFICIAL TRAITS, helping the species adapt.
    """
    print("-" * 80)
    print("  STEP 5: MUTATION — Introducing genetic diversity")
    print("-" * 80)
    mutation_count = 0

    for member in population:
        if random.random() < MUTATION_RATE:
            # Decide which trait to mutate
            trait_to_mutate = random.choice(["Height", "Skin Colour"])

            if trait_to_mutate == "Height":
                change = random.randint(-10, 10)
                member["Height"] = max(140, min(200, member["Height"] + change))
                print(f"    🧬 {member['Name']}: Height mutated by {change:+d} cm")
            else:
                old_skin = member["Skin Colour"]
                member["Skin Colour"] = random.choice(SKIN_COLOURS)
                print(f"    🧬 {member['Name']}: Skin colour mutated"
                      f" ({old_skin} → {member['Skin Colour']})")

            member["Mutation"] = "Yes"
            mutation_count += 1
        else:
            member["Mutation"] = "No"

    print(f"\n  ✓ {mutation_count} members underwent mutation.")
    print(f"  ✓ {len(population) - mutation_count} members remained unchanged.\n")
    return population


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 7: TERMINAL CONDITION — Check if we should stop
# ─────────────────────────────────────────────────────────────────────────────

def check_terminal(generation, max_generations, population):
    """
    Check if the GA should terminate.
    Terminal conditions:
      1. Maximum generations reached
      2. Population fitness has converged (top score > 90)
    """
    top_fitness = population[0]["Fitness Score"]
    avg_fitness = sum(m["Fitness Score"] for m in population) / len(population)

    print("-" * 80)
    print(f"  STEP 7: TERMINAL CHECK — Generation {generation}/{max_generations}")
    print(f"          Top Fitness: {top_fitness:.2f} | Avg Fitness: {avg_fitness:.2f}")
    print("-" * 80)

    if generation >= max_generations:
        print("  ■ TERMINATED: Maximum generations reached.\n")
        return True
    if top_fitness >= 95:
        print("  ■ TERMINATED: Optimal fitness achieved!\n")
        return True

    print("  → Continuing to next generation...\n")
    return False


# ─────────────────────────────────────────────────────────────────────────────
#  STEP 8: DISPLAY RESULT — Print the population table
# ─────────────────────────────────────────────────────────────────────────────

def display_table(population, title="POPULATION TABLE"):
    """Display the population as a formatted table, ranked by fitness score."""
    print("\n" + "=" * 110)
    print(f"  {title}")
    print("=" * 110)
    header = (f"{'S.No':>5} | {'Name':<12} | {'Gender':<7} | {'Height(cm)':>10} | "
              f"{'Skin Colour':<12} | {'Recombination':<14} | {'Mutation':<9} | "
              f"{'Fitness Score':>13}")
    print(header)
    print("-" * 110)

    for member in population:
        row = (f"{member['S.No']:>5} | {member['Name']:<12} | {member['Gender']:<7} | "
               f"{member['Height']:>10} | {member['Skin Colour']:<12} | "
               f"{member['Recombination']:<14} | {member['Mutation']:<9} | "
               f"{member['Fitness Score']:>13.2f}")
        print(row)

    print("-" * 110)

    # Summary statistics
    scores = [m["Fitness Score"] for m in population]
    print(f"\n  📊 STATISTICS:")
    print(f"     Population Size  : {len(population)}")
    print(f"     Highest Fitness  : {max(scores):.2f}")
    print(f"     Lowest Fitness   : {min(scores):.2f}")
    print(f"     Average Fitness  : {sum(scores)/len(scores):.2f}")
    print(f"     Recombined Count : {sum(1 for m in population if m['Recombination'] == 'Yes')}")
    print(f"     Mutated Count    : {sum(1 for m in population if m['Mutation'] == 'Yes')}")
    print()


def display_diversity(population):
    """Show genetic diversity metrics of the population."""
    print("  🌍 GENETIC DIVERSITY ANALYSIS:")
    genders = {}
    skins = {}
    heights = [m["Height"] for m in population]

    for m in population:
        genders[m["Gender"]] = genders.get(m["Gender"], 0) + 1
        skins[m["Skin Colour"]] = skins.get(m["Skin Colour"], 0) + 1

    print(f"     Gender distribution  : {genders}")
    print(f"     Skin colour spread   : {skins}")
    print(f"     Height range         : {min(heights)} cm – {max(heights)} cm")
    print(f"     Height std deviation : {(sum((h - sum(heights)/len(heights))**2 for h in heights) / len(heights)) ** 0.5:.2f} cm")
    print()


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN — Run the Genetic Algorithm Loop
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + " GENETIC ALGORITHM SIMULATION ".center(78) + "║")
    print("║" + " Version 1: Random Population (50 Members) ".center(78) + "║")
    print("║" + " Introduction to Computational Biology — CSE 1st Year ".center(78) + "║")
    print("╚" + "═" * 78 + "╝")

    print("\n  📖 DARWINIAN CONCEPTS OF EVOLUTION DEMONSTRATED:")
    print("     ★ Survival of the Fittest — Only top-ranked members survive selection")
    print("     ★ Beneficial Traits       — Traits closer to ideal yield higher fitness")
    print("     ★ Recombination           — Parents combine traits via crossover")
    print("     ★ Genetic Diversity       — Mutations introduce new trait variations")
    print()

    # ── STEP 1: INITIALIZATION ──
    population = initialize_population(POPULATION_SIZE)

    # ── STEP 2: INITIAL EVALUATION ──
    population = evaluate_population(population, "INITIAL EVALUATION")
    display_table(population, "INITIAL POPULATION (Generation 0) — Ranked by Fitness Score")
    display_diversity(population)

    # ── GA LOOP: SELECTION → RECOMBINATION → MUTATION → EVALUATION → TERMINAL ──
    for generation in range(1, NUM_GENERATIONS + 1):
        print("\n" + "█" * 80)
        print(f"  GENERATION {generation}".center(80))
        print("█" * 80)

        # ── STEP 3: SELECTION ──
        parents = selection(population)

        # ── STEP 4: RECOMBINATION ──
        offspring = recombination(parents, POPULATION_SIZE)

        # ── STEP 5: MUTATION ──
        population = mutation(offspring)

        # ── STEP 6: EVALUATION ──
        population = evaluate_population(population, f"EVALUATION (Generation {generation})")

        # ── STEP 7: TERMINAL CONDITION ──
        if check_terminal(generation, NUM_GENERATIONS, population):
            break

    # ── STEP 8: DISPLAY FINAL RESULT ──
    print("\n" + "█" * 80)
    print("  FINAL RESULT".center(80))
    print("█" * 80)
    display_table(population, f"FINAL POPULATION (After {generation} Generations) — Ranked by Fitness Score")
    display_diversity(population)

    print("  🏆 EVOLUTION SUMMARY:")
    print(f"     The population evolved over {generation} generation(s).")
    print(f"     Fittest individual: {population[0]['Name']} "
          f"(Fitness: {population[0]['Fitness Score']:.2f})")
    print(f"     This demonstrates how natural selection drives populations")
    print(f"     towards better-adapted traits over successive generations.\n")
    print("=" * 80)
    print("  END OF GENETIC ALGORITHM SIMULATION")
    print("=" * 80)


if __name__ == "__main__":
    main()
