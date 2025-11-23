import numpy as np
import matplotlib.pyplot as plt

class Transform2D:
    """2D Transformation Matrix Operations"""
    
    @staticmethod
    def translation(tx, ty):
        """Create 2D translation matrix"""
        return np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ])
    
    @staticmethod
    def rotation(angle_degrees):
        """Create 2D rotation matrix (counter-clockwise)"""
        theta = np.radians(angle_degrees)
        return np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def scaling(sx, sy):
        """Create 2D scaling matrix"""
        return np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def shearing(shx, shy):
        """Create 2D shearing matrix"""
        return np.array([
            [1, shx, 0],
            [shy, 1, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def reflection_x():
        """Create 2D reflection matrix across X-axis"""
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def reflection_y():
        """Create 2D reflection matrix across Y-axis"""
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def reflection_origin():
        """Create 2D reflection matrix about origin (180° rotation)"""
        return np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def reflection_line_y_equals_x():
        """Create 2D reflection matrix across line y=x"""
        return np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def reflection_line_y_equals_minus_x():
        """Create 2D reflection matrix across line y=-x"""
        return np.array([
            [0, -1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ])
    
    @staticmethod
    def apply_transform(points, matrix):
        """Apply transformation matrix to 2D points"""
        # Convert to homogeneous coordinates
        ones = np.ones((1, points.shape[1]))
        homogeneous = np.vstack([points, ones])
        
        # Apply transformation
        transformed = matrix @ homogeneous
        
        # Convert back to 2D
        return transformed[:2, :]


def demo_2d_transformations():
    """Demonstrate 2D transformations on a square"""
    # Define a square
    square = np.array([
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0]
    ])
    
    # Create figure with better spacing (2x3 grid)
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('2D Matrix Transformations (Original: Blue, Transformed: Red)', fontsize=18, fontweight='bold', y=0.98)
    
    # Translation
    trans_matrix = Transform2D.translation(2, 1)
    translated = Transform2D.apply_transform(square, trans_matrix)
    axes[0, 0].plot(square[0], square[1], 'b-', alpha=0.5, linewidth=2, label='Original')
    axes[0, 0].plot(translated[0], translated[1], 'r-', linewidth=2, label='Transformed')
    axes[0, 0].set_title('Translation (tx = 2, ty = 1)', fontsize=12, pad=15)
    axes[0, 0].legend(loc='upper left', fontsize=10)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axis('equal')
    axes[0, 0].set_xlim(-3, 4)
    axes[0, 0].set_ylim(-3, 4)
    axes[0, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # Rotation
    rot_matrix = Transform2D.rotation(45)
    rotated = Transform2D.apply_transform(square, rot_matrix)
    axes[0, 1].plot(square[0], square[1], 'b-', alpha=0.5, linewidth=2, label='Original')
    axes[0, 1].plot(rotated[0], rotated[1], 'r-', linewidth=2, label='Transformed')
    axes[0, 1].set_title('Rotation (45°)', fontsize=12, pad=15)
    axes[0, 1].legend(loc='upper left', fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axis('equal')
    axes[0, 1].set_xlim(-3, 4)
    axes[0, 1].set_ylim(-3, 4)
    axes[0, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 1].axvline(x=0, color='k', linewidth=0.5)
    
    # Scaling
    scale_matrix = Transform2D.scaling(2, 2)
    scaled = Transform2D.apply_transform(square, scale_matrix)
    axes[0, 2].plot(square[0], square[1], 'b-', alpha=0.5, linewidth=2, label='Original')
    axes[0, 2].plot(scaled[0], scaled[1], 'r-', linewidth=2, label='Transformed')
    axes[0, 2].set_title('Scaling (sx = 2, sy = 2)', fontsize=12, pad=15)
    axes[0, 2].legend(loc='upper left', fontsize=10)
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].axis('equal')
    axes[0, 2].set_xlim(-3, 4)
    axes[0, 2].set_ylim(-3, 4)
    axes[0, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[0, 2].axvline(x=0, color='k', linewidth=0.5)
    
    # Shearing
    shear_matrix = Transform2D.shearing(2, 0)
    sheared = Transform2D.apply_transform(square, shear_matrix)
    axes[1, 0].plot(square[0], square[1], 'b-', alpha=0.5, linewidth=2, label='Original')
    axes[1, 0].plot(sheared[0], sheared[1], 'r-', linewidth=2, label='Transformed')
    axes[1, 0].set_title('Shearing (shx = 2)', fontsize=12, pad=15)
    axes[1, 0].legend(loc='upper left', fontsize=10)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axis('equal')
    axes[1, 0].set_xlim(-3, 4)
    axes[1, 0].set_ylim(-3, 4)
    axes[1, 0].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 0].axvline(x=0, color='k', linewidth=0.5)
    
    # Reflection about Origin
    reflect_origin_matrix = Transform2D.reflection_origin()
    reflected_origin = Transform2D.apply_transform(square, reflect_origin_matrix)
    axes[1, 1].plot(square[0], square[1], 'b-', alpha=0.5, linewidth=2, label='Original')
    axes[1, 1].plot(reflected_origin[0], reflected_origin[1], 'r-', linewidth=2, label='Transformed')
    axes[1, 1].scatter([0], [0], color='purple', s=200, marker='x', linewidth=3, 
                      label='Origin', zorder=5)
    axes[1, 1].set_title('Reflection about Origin', fontsize=12, pad=15)
    axes[1, 1].legend(loc='upper right', fontsize=10)
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axis('equal')
    axes[1, 1].set_xlim(-3, 4)
    axes[1, 1].set_ylim(-3, 4)
    axes[1, 1].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 1].axvline(x=0, color='k', linewidth=0.5)
    
    # Combined transformations
    combined = Transform2D.rotation(45) @ Transform2D.scaling(2, 2) @ Transform2D.translation(2, 1)
    combined_result = Transform2D.apply_transform(square, combined)
    axes[1, 2].plot(square[0], square[1], 'b-', alpha=0.5, linewidth=2, label='Original')
    axes[1, 2].plot(combined_result[0], combined_result[1], 'r-', linewidth=2, label='Transformed')
    axes[1, 2].set_title('Combined\n(Translate * Scale * Rotate)', fontsize=12, pad=15)
    axes[1, 2].legend(loc='upper left', fontsize=10)
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].axis('equal')
    axes[1, 2].set_xlim(-3, 4)
    axes[1, 2].set_ylim(-3, 8)
    axes[1, 2].axhline(y=0, color='k', linewidth=0.5)
    axes[1, 2].axvline(x=0, color='k', linewidth=0.5)
    
    # Adjust layout to prevent overlap
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.subplots_adjust(hspace=0.35, wspace=0.3)
    plt.show()


if __name__ == "__main__":
    print("=" * 60)
    print("2D MATRIX TRANSFORMATIONS FOR GRAPHICS")
    print("=" * 60)
    
    print("\n2D Transformation Matrices:")
    print("---------------------------")
    
    print("\n1. Translation Matrix (tx=2, ty=1):")
    print(Transform2D.translation(2, 1))
    
    print("\n2. Rotation Matrix (45°):")
    print(Transform2D.rotation(45))
    
    print("\n3. Scaling Matrix (sx=2, sy=0.5):")
    print(Transform2D.scaling(2, 0.5))
    
    print("\n4. Shearing Matrix (shx=0.5, shy=0):")
    print(Transform2D.shearing(0.5, 0))
    
    print("\n5. Reflection Matrix (X-axis):")
    print(Transform2D.reflection_x())
    
    print("\n6. Reflection Matrix (Y-axis):")
    print(Transform2D.reflection_y())
    
    print("\n7. Reflection Matrix (Origin):")
    print(Transform2D.reflection_origin())
    
    print("\n8. Reflection Matrix (y=x line):")
    print(Transform2D.reflection_line_y_equals_x())
    
    print("\n9. Reflection Matrix (y=-x line):")
    print(Transform2D.reflection_line_y_equals_minus_x())
    
    # Example: Applying transformations
    print("\n" + "=" * 60)
    print("Example: Transforming a point (2, 3)")
    print("=" * 60)
    
    point = np.array([[2], [3]])
    
    # Translation
    translated = Transform2D.apply_transform(point, Transform2D.translation(1, 2))
    print(f"\nAfter Translation (1, 2): ({translated[0][0]:.2f}, {translated[1][0]:.2f})")
    
    # Rotation
    rotated = Transform2D.apply_transform(point, Transform2D.rotation(90))
    print(f"After Rotation (90°): ({rotated[0][0]:.2f}, {rotated[1][0]:.2f})")
    
    # Scaling
    scaled = Transform2D.apply_transform(point, Transform2D.scaling(2, 0.5))
    print(f"After Scaling (2, 0.5): ({scaled[0][0]:.2f}, {scaled[1][0]:.2f})")
    
    # Reflection about X-axis
    reflected_x = Transform2D.apply_transform(point, Transform2D.reflection_x())
    print(f"After Reflection X-axis: ({reflected_x[0][0]:.2f}, {reflected_x[1][0]:.2f})")
    
    # Reflection about Origin
    reflected_origin = Transform2D.apply_transform(point, Transform2D.reflection_origin())
    print(f"After Reflection Origin: ({reflected_origin[0][0]:.2f}, {reflected_origin[1][0]:.2f})")
    
    print("\n" + "=" * 60)
    print("Displaying 2D transformations...")
    print("=" * 60)
    demo_2d_transformations()