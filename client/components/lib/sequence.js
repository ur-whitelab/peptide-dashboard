import {event, select} from 'd3-selection'
import {forceSimulation, forceManyBody, forceCenter, forceLink, forceX, forceY} from 'd3-force'
import {drag} from 'd3-drag'

class SequenceD3 {
  constructor (canvas) {
    this.context = canvas.getContext('2d')
    this.width = canvas.width
    this.height = canvas.height

    this.simulation = forceSimulation()
      .force('link', forceLink().distance(this.width / 20))
      .force('charge', forceManyBody())
      .force('x', forceX().strength(0.0))
      .force('y', forceY().strength(0.0))
      .force('center', forceCenter(this.width / 2, this.height / 2))

    select(canvas)
      .call(drag()
        .container(canvas)
        .subject(() => this.simulation.find(event.x, event.y))
        .on('start', () => {
          if (!event.active) this.simulation.alphaTarget(0.3).restart()
          event.subject.fx = event.subject.x
          event.subject.fy = event.subject.y
        })
        .on('drag', () => {
          event.subject.fx = event.x
          event.subject.fy = event.y
        })
        .on('end', () => {
          if (!event.active) this.simulation.alphaTarget(0)
          event.subject.fx = null
          event.subject.fy = null
        }))

    this.simulation.on('tick', this.ticked.bind(this))
    this.update('')
  }

  update (sequence) {
    this.nodes = sequence.split('').map((x, i) => { return {name: x, id: i, y: 0, x: i * this.width / sequence.length - this.width / 2} })
    // keep data for existing nodes

    // give new one a kick
    if (this.nodes.length > 0)
      this.nodes[this.nodes.length - 1].vx = 0.0

    // adjust centering force
    if (sequence.length > 10) {
      this.simulation.force('x').strength(Math.min(0.05, this.nodes.length * 0.05 / 50))
      this.simulation.force('y').strength(Math.min(0.1, this.nodes.length * 0.1 / 50))
    }

    this.simulation.nodes(this.nodes)
    this.links = this.simulation.nodes().slice(0, -1).map((n, i) => { return {source: i, target: i + 1} })
    this.simulation.force('link').links(this.links)
    this.simulation.force('link').distance(this.width / this.nodes.length)
    this.simulation.alphaTarget(0.3).restart()
  }

  ticked () {
    this.context.clearRect(0, 0, this.width, this.height)

    this.context.beginPath()
    this.nodes.slice(0, -1).forEach((d, i) => {
      this.context.moveTo(d.x, d.y)
      this.context.lineTo(this.nodes[i + 1].x, this.nodes[i + 1].y)
    })
    this.context.strokeStyle = '#aaa'
    this.context.stroke()

    this.context.beginPath()
    this.nodes.forEach((d) => {
      this.context.moveTo(d.x + 3, d.y)
      this.context.arc(d.x, d.y, 3, 0, 2 * Math.PI)
    })
    this.context.fill()
    this.context.strokeStyle = '#fff'
    this.context.stroke()
  }
}

export default SequenceD3
