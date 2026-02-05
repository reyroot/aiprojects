#This is a training loop simulation     

predictions = [0.25, 0.60, 0.95, 0.48]
targets = [0.0, 0.5, 1.0, 0.0]

total_error = 0

print("--- Star error analysis ---")

for i, (pred, target)  in enumerate(zip(predictions, targets)):
    error = abs(pred - target)
    total_error += error
    print(f"Sample {i}: Pred={pred}, Target={target}, Error={error:.2f}")

print(f"Total error: {total_error}")






