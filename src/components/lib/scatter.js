import {scaleLinear} from 'd3-scale'
import {axisBottom, axisLeft} from 'd3-axis'
import {line, area} from 'd3-shape'
import {min, max} from 'd3-array'
import {select} from 'd3-selection'
import 'd3-transition'

class Scatter {
  constructor () {
    this.margin = 100
    this.labelMargin = 50
  }

  draw (root, width, height, xlabel, ylabel) {
    this.width -= this.margin + this.labelMargin
    this.height -= this.margin + this.labelMargin
    this.svg = select(root).append('svg')
      .attr('width', width + this.margin + this.labelMargin)
      .attr('height', height + this.margin + this.labelMargin)
      .style('background', '#FFF')
    this.width = width
    this.height = height

    this.svg.append('rect')
      .attr('width', this.width + this.margin)
      .attr('height', this.height + this.margin)
      .classed('margin', true)

    this.plot_group = this.svg.append('g')
      .attr('transform',
        'translate(' + (this.margin / 2 + this.labelMargin) +
        ',' + (this.margin / 2) + ')')

    this.plot_group.append('rect')
      .attr('width', this.width)
      .attr('height', this.height)
      .classed('canvas', true)

    this.xScale = scaleLinear().domain(
      [1, 10])
      .range([0, this.width])

    this.yScale = scaleLinear().domain(
      [0, 1])
      .range([this.height, 25])

    this.xAxis = axisBottom().scale(this.xScale)
    this.yAxis = axisLeft().scale(this.yScale).ticks(4)

    // Add the x-axis.
    this.plot_group.append('g')
      .attr('class', 'x axis')
      .attr('transform', 'translate(0,' + this.height + ')')
      .call(this.xAxis)

    this.plot_group.append('text')
      .attr('class', 'x label')
      .attr('text-anchor', 'middle')
      .attr('x', this.width / 2)
      .attr('y', this.height + this.margin / 2)
      .text(xlabel)

    // Add the y-axis.
    this.plot_group.append('g')
      .attr('class', 'y axis')
      .call(this.yAxis)

    this.plot_group.append('text')
      .attr('class', 'y label')
      .attr('text-anchor', 'middle')
      .attr('transform', 'translate(' + (-this.margin / 2) + ', ' + this.height / 2 + ') rotate(-90)')
      .text(ylabel)

    this.lineFxn = line()
      .x((d) => {
        return this.xScale(d[0])
      })
      .y((d) => {
        return this.yScale(d[1])
      })
    this.plot_group.append('path').attr('d', this.lineFxn([])).classed('line', true)

    this.areaFxn = area()
      .x((d) => {
        return this.xScale(d[0])
      })
      .y0(this.height)
      .y1((d) => {
        return this.yScale(d[1])
      })
    this.plot_group.append('path')
      .attr('d', this.areaFxn([])).classed('line-area', true)
  }

  plot (data, delay) {
    // this updates our plotting scale
    this.xScale = scaleLinear().domain(
      [min(data
        .map(function (x) {
          return x[0]
        })),
      max(data
        .map(function (x) {
          return x[0]
        }))
      ])
      .range([0, this.width])

    this.yScale = scaleLinear().domain(
      [min(data
        .map(function (x) {
          return x[1]
        })),
      max(data
        .map(function (x) {
          return x[1]
        }))
      ])
      .range([this.height, 25])

      // recomputes ticks
    this.xAxis = axisBottom().scale(this.xScale)
    this.yAxis = axisLeft().scale(this.yScale).ticks(4)

    // updates lines
    this.plot_group.transition().select('.line').duration(delay).attr('d', this.lineFxn(data))

    // update circles (see above for more notes)
    let xScale = this.xScale
    let yScale = this.yScale
    let that = this
    let updateSel = this.plot_group.selectAll('circle')
      .data(data, (d) => { return d })
    updateSel
      .enter().append('circle')
      .attr('cx', (d) => { return xScale(d[0]) })
      .attr('cy', (d) => { return yScale(d[1]) })
      .attr('r', 5)
      .attr('opacity', 0)
      .classed('circle', true)
    updateSel
      .exit().remove()

    this.plot_group.transition()
      .selectAll('circle')
      .duration(delay / 4)
      .attr('opacity', 0)
      .on('end', function () {
        updateSel
          .attr('cx', (d) => { return xScale(d[0]) })
          .attr('cy', (d) => { return yScale(d[1]) })
        that.plot_group.transition().selectAll('circle').delay(delay / 4).duration(delay).attr('opacity', 1)
      })

    this.plot_group.transition().select('.line-area').duration(delay / 4).style('opacity', 0).on('end', function () {
      that.plot_group.select('.line-area').attr('d', that.areaFxn(data))
      that.plot_group.transition().select('.line-area').delay(delay / 4).duration(delay / 2).style('opacity', 0.2)
    })

    this.plot_group.transition().select('.y.axis').duration(delay).call(this.yAxis)
    this.plot_group.transition().select('.x.axis').duration(delay).call(this.xAxis)
  }

  select (i) {
    return null
  }
}

export default Scatter
