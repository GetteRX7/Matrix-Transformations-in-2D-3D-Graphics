import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Transform3D:
    """3D Transformation Matrix Operations"""
    
    @staticmethod
    def translation(tx, ty, tz):
        return np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_x(angle_degrees):
        theta = np.radians(angle_degrees)
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(theta), -np.sin(theta), 0],
            [0, np.sin(theta), np.cos(theta), 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def scaling(sx, sy, sz):
        return np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def shear_x(shx):
        return np.array([
            [1, shx, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def reflection_x():
        return np.array([
            [1, 0, 0, 0],
            [0, -1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def reflection_y():
        return np.array([
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def reflection_origin():
        return np.array([
            [-1, 0, 0, 0],
            [0, -1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def combined_transform():
        """Example: Combined Translation + Rotation X + Scaling"""
        return Transform3D.translation(1, 1, 0.5) @ Transform3D.rotation_x(30) @ Transform3D.scaling(1.2, 0.8, 1.5)
    
    @staticmethod
    def apply_transform(points, matrix):
        ones = np.ones((1, points.shape[1]))
        homogeneous = np.vstack([points, ones])
        transformed = matrix @ homogeneous
        return transformed[:3, :]


def plot_cube(ax, cube, edges, color, linestyle='-', label=None):
    for edge in edges:
        pts = cube[:, edge]
        ax.plot3D(pts[0], pts[1], pts[2], color=color, linestyle=linestyle, linewidth=2, label=label if edge == edges[0] else "")


def demo_3d_transformations():
    cube = np.array([
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1]
    ])
    
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]
    
    fig = plt.figure(figsize=(20, 14))
    fig.suptitle('3D Transformations (Original: Blue, Transformed: Red)', 
                 fontsize=18, fontweight='bold', y=0.985)
    
    def plot_with_original(ax, transform_matrix, title):
        transformed = Transform3D.apply_transform(cube, transform_matrix)
        plot_cube(ax, cube, edges, 'blue', '-', label='Original')
        plot_cube(ax, transformed, edges, 'red', '-', label='Transformed')
        ax.legend(loc='upper right', fontsize=9)
        ax.set_title(title, pad=25, fontsize=12)
        ax.set_xlim([-3, 3]); ax.set_ylim([-3, 3]); ax.set_zlim([-3, 3])
        ax.set_xlabel('X', labelpad=12)
        ax.set_ylabel('Y', labelpad=12)
        ax.set_zlabel('Z', labelpad=12)
    
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    plot_with_original(ax1, Transform3D.translation(2, 1, 0.5), 'Translation (2,1,0.5)')
    
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    plot_with_original(ax2, Transform3D.rotation_x(45), 'Rotation X-axis (45°)')
    
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    plot_with_original(ax3, Transform3D.scaling(2, 2, 1.5), 'Scaling (2,2,1.5)')
    
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')
    plot_with_original(ax4, Transform3D.shear_x(2), 'Shearing (Shx=2)')
    
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')
    plot_with_original(ax5, Transform3D.reflection_origin(), 'Reflection Through Origin')
    
    ax6 = fig.add_subplot(2, 3, 6, projection='3d')
    plot_with_original(ax6, Transform3D.combined_transform(), 'Combined Transformation')
    
    plt.tight_layout(rect=[0, 0.01, 1, 0.96], h_pad=5, w_pad=3)
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    plt.show()


if __name__ == "__main__":
    demo_3d_transformations()