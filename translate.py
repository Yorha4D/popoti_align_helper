import bpy


translations_dict = {
    "zh_CN": {
        ("上下文", "原文"): "翻译文字",
        ("*", "3D View: POPOTI Align Helper"): "3D 视图: POPOTI对齐助手",
        ("*", "POPOTI Align Helper"): "POPOTI对齐助手",
        ("Operator", "POPOTI Align Helper"): "POPOTI对齐助手",
        ("Operator", "Word Original"): "世界原点",
        ("*", "Word Original"): "世界原点",
        ("*", "More friendly alignment based on observation perspective"): "更友好的基于观察视角的对齐",
        ("*", "Tool Panel"): "工具面板",
        ("*", "Axis to be aligned"): "需要对齐的轴",
        ("*", "Select the axis to be aligned, multiple choices are allowed"): "选择需要进行对齐的轴,可多选",
        ("*", "Align X Axis"): "对齐X轴",
        ("*", "Align Y Axis"): "对齐Y轴",
        ("*", "Align Z Axis"): "对齐Z轴",
        ("*", "Min Point"): "最小点",
        ("*", "Max Point"): "最大点",
        ("*", "Center Align"): "中心对齐",
        ("*", "Align to Min Point"): "对齐到最小点",
        ("*", "Align to Max Point"): "对齐到最大点",
        ("*", "Distribution"): "分布",
        ("*", "Distribution Align"): "分布对齐",
        ("*", "General alignment, you can set the alignment of each axis(maximum, center, minimum)"): "常规对齐,可以设置每个轴的对齐方式(最大,居中,最小)",
        ("*", "Align to Cursor(Scale reset 1)"): "对齐到游标(缩放将重置为1)",
        ("*", "Align to Active Object"): "对齐到活动物体",
        ("*", "Aligning to the world origin is the same as resetting"): "对齐到世界原点,和重置功能相同",
        ("*", "Sort distribution by X axis"): "按X轴排序分布",
        ("*", "Sort distribution by Y axis"): "按Y轴排序分布",
        ("*", "Sort distribution by Z axis"): "按Z轴排序分布",
        ("*", "Align and sort the selected objects according to the selection axis to obtain the correct movement position"): "按选择轴对所选物体进行对齐并排序,以获取正确的移动位置",
        ("*", "Distribution sort axis"): "分布排序轴",
        ("*", "Lowest Object"): "最低物体",
        ("*", "All Object"): "所有物体",
        ("*", "Sort Axis"): "排序轴",
    }
}

def register():
    bpy.app.translations.register(__name__, translations_dict)


def unregister():
    bpy.app.translations.unregister(__name__)
