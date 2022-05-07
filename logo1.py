import cairo
from math import pi

W = 16  # Sides of basic squares
WIDTH, HEIGHT = 12 * W, 3 * W

surface = cairo.SVGSurface("logo1.svg", WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)  # white background
ctx.paint()

empty_points = {
    (4, 0),
    (0, 1),
    (2, 1),
    (5, 1),
    (8, 1),
    (9, 1),
    (11, 1),
    (0, 2),
    (2, 2),
    (4, 2),
    (9, 2),
    (11, 2),
}
solid_points = set(
    (x, y) for x in range(12) for y in range(3) if (x, y) not in empty_points
)
edges = {
    # T:
    ((0, 0), (1, 0)),
    ((1, 0), (2, 0)),
    ((1, 0), (1, 1)),
    ((1, 1), (1, 2)),
    # K:
    ((3, 0), (3, 1)),
    ((3, 1), (4, 1)),
    ((4, 1), (5, 0)),
    ((3, 1), (3, 2)),
    ((4, 1), (5, 2)),
    # E:
    ((6, 0), (7, 0)),
    ((7, 0), (8, 0)),
    ((6, 0), (6, 1)),
    ((6, 1), (7, 1)),
    ((6, 1), (6, 2)),
    ((6, 2), (7, 2)),
    ((7, 2), (8, 2)),
    # T:
    ((9, 0), (10, 0)),
    ((10, 0), (11, 0)),
    ((10, 0), (10, 1)),
    ((10, 1), (10, 2)),
}


def as_coords(point):
    x, y = point
    return ((x + 0.5) * W, (y + 0.5) * W)


def draw_line(ctx, edge):
    p0, p1 = edge
    x0, y0 = as_coords(p0)
    x1, y1 = as_coords(p1)
    ctx.move_to(x0, y0)
    ctx.line_to(x1, y1)
    ctx.set_line_width(0.125 * W)
    ctx.set_source_rgb(0, 0, 0)  # black
    ctx.stroke()


def draw_solid_point(ctx, point):
    x, y = as_coords(point)
    ctx.arc(x, y, 0.25 * W, 0, 2 * pi)
    ctx.set_source_rgb(0, 0, 0)  # black
    ctx.fill()


def draw_empty_point(ctx, point):
    x, y = as_coords(point)
    ctx.arc(x, y, 0.25 * W, 0, 2 * pi)
    ctx.set_source_rgb(1, 0.5, 0)
    ctx.fill()


for edge in edges:
    draw_line(ctx, edge)

for point in solid_points:
    draw_solid_point(ctx, point)

for point in empty_points:
    draw_empty_point(ctx, point)


surface.write_to_png("logo1.png")
surface.finish()
