import numpy as np
import matplotlib.pyplot as plt

def calculate_weights():
    """Calculates fundamental geometric constants for M4 projection."""
    constants = {
        "sqrt_2": np.sqrt(2),
        "sqrt_3": np.sqrt(3),
        "sqrt_5": np.sqrt(5)
    }
    return constants

def plot_vesica_piscis():
    """Renders the Vesica Piscis interface."""
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Circle centers at distance r (let r=1)
    x1, y1 = -0.5, 0
    x2, y2 = 0.5, 0
    
    circle1_x = 0.5 * np.cos(theta) + x1
    circle1_y = 0.5 * np.sin(theta) + y1
    
    circle2_x = 0.5 * np.cos(theta) + x2
    circle2_y = 0.5 * np.sin(theta) + y2
    
    plt.figure(figsize=(6,6))
    plt.plot(circle1_x, circle1_y, label='Brane A (Source)')
    plt.plot(circle2_x, circle2_y, label='Brane B (Runtime)')
    plt.fill_betweenx(y=[-0.433, 0.433], x1=[-0.25, 0.25], color='skyblue', alpha=0.3, label='Intersection (Vesica)')
    
    plt.title("Vesica Piscis: Primary Compiler Lens")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    weights = calculate_weights()
    print("--- Aegis Protocol: System Weight Tables ---")
    for key, val in weights.items():
        print(f"{key}: {val:.10f}")
    
    plot_vesica_piscis()
  
