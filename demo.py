#!/usr/bin/env python3
"""
Demo script to simulate the data processing workflow with sample data.
This helps users understand how the system works without needing Kaggle API access.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import os

def create_sample_data():
    """Create sample NASA-style software defect prediction data."""
    np.random.seed(42)  # For reproducible results
    
    # Create sample data that mimics NASA software metrics
    n_samples = 1000
    
    # Generate sample metrics (typical software complexity metrics)
    data = {
        'loc': np.random.randint(10, 10000, n_samples),  # Lines of code
        'v_g': np.random.randint(1, 50, n_samples),       # Cyclomatic complexity
        'ev_g': np.random.randint(1, 100, n_samples),     # Essential complexity
        'iv_g': np.random.randint(1, 30, n_samples),      # Design complexity
        'n': np.random.randint(5, 500, n_samples),        # Total operators + operands
        'v': np.random.randint(10, 2000, n_samples),      # Volume
        'd': np.random.randint(1, 100, n_samples),        # Difficulty
        'i': np.random.randint(1, 50, n_samples),         # Intelligence
        'e': np.random.randint(50, 50000, n_samples),     # Effort
        'b': np.random.randint(1, 1000, n_samples),       # Bugs
        't': np.random.randint(1, 3000, n_samples),       # Time
        'lOCode': np.random.randint(5, 8000, n_samples),  # Lines of code
        'lOComment': np.random.randint(0, 2000, n_samples), # Lines of comments
        'lOBlank': np.random.randint(0, 1000, n_samples), # Blank lines
        'lOCodeAndComment': np.random.randint(0, 100, n_samples), # Mixed lines
        'uniq_Op': np.random.randint(1, 50, n_samples),   # Unique operators
        'uniq_Opnd': np.random.randint(1, 100, n_samples), # Unique operands
        'total_Op': np.random.randint(10, 1000, n_samples), # Total operators
        'total_Opnd': np.random.randint(10, 2000, n_samples), # Total operands
        'branchCount': np.random.randint(0, 200, n_samples), # Branch count
    }
    
    # Create defect indicator (binary classification)
    # Higher complexity metrics increase defect probability
    complexity_score = (
        data['v_g'] / 50 + 
        data['ev_g'] / 100 + 
        data['d'] / 100 + 
        data['loc'] / 10000
    )
    
    # Add some noise and create binary defect indicator
    defect_prob = 1 / (1 + np.exp(-2 * (complexity_score - 0.5)))
    data['defects'] = np.random.binomial(1, defect_prob, n_samples)
    
    return pd.DataFrame(data)

def simulate_data_processing():
    """Simulate the complete data processing workflow."""
    print("NASA Software Defect Prediction - Demo Mode")
    print("=" * 50)
    
    # Setup directories
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    raw_dir = data_dir / "raw"
    processed_dir = data_dir / "processed"
    metadata_dir = data_dir / "metadata"
    
    # Create directories
    for directory in [raw_dir, processed_dir, metadata_dir]:
        directory.mkdir(parents=True, exist_ok=True)
    
    print("✓ Created data directories")
    
    # Create multiple sample datasets (simulating different NASA projects)
    datasets = {
        'kc1': create_sample_data(),
        'kc2': create_sample_data(),
        'pc1': create_sample_data(),
        'pc2': create_sample_data(),
        'cm1': create_sample_data(),
    }
    
    print(f"✓ Generated {len(datasets)} sample datasets")
    
    # Save datasets as CSV files
    for name, df in datasets.items():
        csv_file = processed_dir / f"{name}.csv"
        df.to_csv(csv_file, index=False)
        print(f"✓ Saved {name}.csv ({df.shape[0]} rows, {df.shape[1]} columns)")
    
    # Create metadata
    metadata_info = {
        "dataset_name": "NASA Software Defect Prediction (Demo Data)",
        "source": "Generated sample data for demonstration",
        "description": "Sample NASA-style software defect prediction datasets",
        "files": []
    }
    
    for name, df in datasets.items():
        file_info = {
            "filename": f"{name}.csv",
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "data_types": df.dtypes.astype(str).to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "defect_rate": f"{df['defects'].mean():.2%}",
            "description": f"Sample NASA {name.upper()} dataset with {len(df)} samples"
        }
        metadata_info["files"].append(file_info)
    
    # Save metadata
    metadata_file = metadata_dir / "dataset_info.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata_info, f, indent=2)
    
    print(f"✓ Created metadata file: {metadata_file.name}")
    
    # Display summary
    print("\nDataset Summary:")
    print("-" * 30)
    total_samples = sum(len(df) for df in datasets.values())
    avg_defect_rate = np.mean([df['defects'].mean() for df in datasets.values()])
    
    print(f"Total datasets: {len(datasets)}")
    print(f"Total samples: {total_samples}")
    print(f"Average defect rate: {avg_defect_rate:.2%}")
    
    # Show example data
    print("\nExample data from kc1.csv:")
    print(datasets['kc1'].head())
    
    print("\n" + "=" * 50)
    print("Demo completed successfully!")
    print("You can now run 'python scripts/analyze_data.py' to analyze the data.")

def main():
    """Main function."""
    simulate_data_processing()

if __name__ == "__main__":
    main()