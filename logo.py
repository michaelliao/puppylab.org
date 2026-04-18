#!/usr/bin/env python3

import math

def main():
    head = gen_head_path()
    eyel, eyer, nose = gen_circles()
    f1, f2, fb = gen_face_paths()
    svg = '<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">\n'
    svg = svg + f'  <g stroke="#000000" stroke-width="2" stroke-linecap="round" fill="#ffffff">\n'
    svg = svg + f'    {head}\n'
    svg = svg + f'  </g>\n'
    svg = svg + f'  <g fill="#000000">\n'
    svg = svg + f'    {eyel}\n'
    svg = svg + f'    {eyer}\n'
    svg = svg + f'    {nose}\n'
    svg = svg + f'  </g>\n'
    svg = svg + f'  <g stroke="#000000" stroke-width="3" stroke-linecap="round">\n'
    svg = svg + f'    {f1}\n'
    svg = svg + f'    {f2}\n'
    svg = svg + f'    {fb}\n'
    svg = svg + f'  </g>\n'
    svg = svg + f'</svg>\n'
    with open('logo.svg', 'w') as f:
        f.write(svg)
    print(svg)

def gen_head_path(cx=60, cy=60):
    r_anchor = 55          # 锚点半径（路径经过的点）
    r_control = 65         # 控制点半径（拉伸曲线的点）
    segments = 16          # 曲线段数
    
    path_data = []
    
    # 起始点 (0度方向)
    start_x = cx + r_anchor * math.cos(0)
    start_y = cy + r_anchor * math.sin(0)
    path_data.append(f"M {start_x:.4g} {start_y:.4g}")
    
    for i in range(segments):
        # 计算角度 (SVG 坐标系中顺时针或逆时针，这里原数据是逆着 y 轴减小方向走的)
        # 原数据第一步从 (115, 60) 到 (110.8, 38.9)，说明角度在减小
        angle_step = 2 * math.pi / segments
        
        # 当前段的控制点角度 (位于两个锚点中间)
        ctrl_angle = -(i + 0.5) * angle_step
        # 当前段的终点角度
        end_angle = -(i + 1) * angle_step
        
        # 控制点坐标
        cx_p = cx + r_control * math.cos(ctrl_angle)
        cy_p = cy + r_control * math.sin(ctrl_angle)
        
        # 终点坐标
        ex = cx + r_anchor * math.cos(end_angle)
        ey = cy + r_anchor * math.sin(end_angle)
        
        path_data.append(f"Q {cx_p:.6g} {cy_p:.6g}, {ex:.6g} {ey:.6g}")
    
    d = " ".join(path_data)
    return f'<path d="{d}" />'

def gen_circles(cx=60, cy=60):
    # 配置参数
    eye_offset_x = 17
    eye_offset_y = -5
    eye_radius = 6

    nose_offset_y = 13
    nose_radius = 8
    
    # 计算具体坐标
    circles = [
        # 左眼
        {"cx": cx - eye_offset_x, "cy": cy + eye_offset_y, "r": eye_radius},
        # 右眼
        {"cx": cx + eye_offset_x, "cy": cy + eye_offset_y, "r": eye_radius},
        # 鼻子/中心点
        {"cx": cx, "cy": cy + nose_offset_y, "r": nose_radius}
    ]
    
    # 转换为 SVG 字符串
    svg_elements = []
    for c in circles:
        ccx = c["cx"]
        ccy = c["cy"]
        cr = c["r"]
        svg_elements.append(f'<circle cx="{ccx:.6g}" cy="{ccy:.6g}" r="{cr:.6g}" />')

    return svg_elements

def gen_face_paths(cx=60, cy=60):
    # 根据中心点偏移计算坐标 (原图基于 121x121，中心约为 60, 60)
    # 嘴巴的基准高度在 cy + 20 (即 80) 和 cy + 25 (即 85)
    
    # 1. 左嘴角 (Left Smile)
    # M 40 80 Q 43 85, 50 85
    p1 = f"M {cx-20} {cy+20} Q {cx-17} {cy+25}, {cx-10} {cy+25}"
    
    # 2. 右嘴角 (Right Smile)
    # M 80 80 Q 77 85, 70 85
    p2 = f"M {cx+20} {cy+20} Q {cx+17} {cy+25}, {cx+10} {cy+25}"
    
    # 3. 嘴部连接线 + 舌头 (Mouth Middle + Tongue)
    # 舌头颜色: #DC143C
    # Q段构成 w 的中间，C段构成 U 形舌头
    p3 = (f"M {cx-10:.6g} {cy+25:.6g} "
          f"Q {cx-3:.6g} {cy+25:.6g}, {cx:.6g} {cy+20:.6g} "
          f"Q {cx+3:.6g} {cy+25:.6g}, {cx+10:.6g} {cy+25:.6g} "
          f"C {cx+10:.6g} {cy+40:.6g}, {cx-10:.6g} {cy+40:.6g}, {cx-10:.6g} {cy+25:.6g}")
    
    return (
        f'<path d="{p1}" fill="transparent" />',
        f'<path d="{p2}" fill="transparent" />',
        f'<path d="{p3}" fill="#dc143c" />'
    )

if __name__ == '__main__':
    main()
