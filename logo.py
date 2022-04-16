import cairo

W = 16  # Thickness of lines of T
WIDTH, HEIGHT = 12 * W, 8 * W

surface = cairo.SVGSurface("logo.svg", WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1)  # white background
ctx.paint()


def draw_TT(ctx):
    ctx.move_to(W, W)
    ctx.line_to(11 * W, W)
    ctx.line_to(11 * W, 2 * W)
    ctx.line_to(9 * W, 2 * W)
    ctx.line_to(9 * W, 7 * W)
    ctx.line_to(8 * W, 7 * W)
    ctx.line_to(8 * W, 2 * W)
    ctx.line_to(4 * W, 2 * W)
    ctx.line_to(4 * W, 7 * W)
    ctx.line_to(3 * W, 7 * W)
    ctx.line_to(3 * W, 2 * W)
    ctx.line_to(W, 2 * W)
    ctx.line_to(W, W)


def draw_KE(ctx):
    ctx.move_to(4 * W, 2 * W)
    ctx.line_to(5 * W, 2 * W)
    ctx.line_to(5 * W, 4 * W)
    ctx.line_to(7 * W, 2 * W)
    ctx.line_to(8 * W, 2 * W)
    ctx.line_to(8 * W, 3 * W)
    ctx.line_to(7.25 * W, 3 * W)
    ctx.line_to(6.25 * W, 4 * W)
    ctx.line_to(7.5 * W, 4 * W)
    ctx.line_to(7.5 * W, 5 * W)
    ctx.line_to(6.25 * W, 5 * W)
    ctx.line_to(7.25 * W, 6 * W)
    ctx.line_to(8 * W, 6 * W)
    ctx.line_to(8 * W, 7 * W)
    ctx.line_to(7 * W, 7 * W)
    ctx.line_to(5 * W, 5 * W)
    ctx.line_to(5 * W, 7 * W)
    ctx.line_to(4 * W, 7 * W)
    ctx.line_to(4 * W, 2 * W)


draw_TT(ctx)
ctx.set_source_rgb(0.75, 0, 0)  # red
ctx.fill()

draw_KE(ctx)
ctx.set_source_rgb(0, 0.75, 0)  # green
ctx.fill()

ctx.set_line_width(0.125 * W)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
ctx.set_source_rgb(0, 0, 0)  # black borders

draw_TT(ctx)
ctx.stroke()

draw_KE(ctx)
ctx.stroke()

surface.write_to_png("logo.png")
surface.finish()
