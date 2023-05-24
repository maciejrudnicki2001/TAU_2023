describe('Add to Cart', () => {
    it('Adds a product to the cart', () => {
      cy.visit('https://www.saucedemo.com/')
      cy.get('#user-name').type('standard_user')
      cy.get('#password').type('secret_sauce')
      cy.get('#login-button').click()
      cy.get('.inventory_item')
        .each((product) => {
          cy.wrap(product)
            .find('.btn_inventory')
            .click()
        })
      cy.get('.shopping_cart_link').click()
      cy.get('.cart_item').should('have.length', 6)
    })
  })
  