def even_lines(io_object):
  return [line.strip() for (i,line) in enumerate(io_object) if (i+1) %2==0]