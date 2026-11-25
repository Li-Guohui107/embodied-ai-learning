"""A tiny observation-decision-action-feedback loop."""


def observe(position, goal):
    return {"position": position, "goal": goal}


def decide(observation):
    if observation["position"] < observation["goal"]:
        return 1
    if observation["position"] > observation["goal"]:
        return -1
    return 0


def act(position, action):
    return position + action


def main():
    position, goal = 0, 5
    for step in range(10):
        observation = observe(position, goal)
        action = decide(observation)
        print(f"step={step:02d} position={position} goal={goal} action={action}")
        if action == 0:
            print("Goal reached.")
            break
        position = act(position, action)


if __name__ == "__main__":
    main()
